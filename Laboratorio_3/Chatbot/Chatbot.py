import streamlit as st
from streamlit_mic_recorder import speech_to_text
from langchain_deepseek import ChatDeepSeek
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from gtts import gTTS
import io
import base64
import os #necesario para key en hugging face

# --- Configuración de la página ---
st.set_page_config(
    page_title="Chat Completo modo Santaolalla",
    page_icon="⚛️",
    layout="centered"
)

# --- Título y Descripción ---
st.title("Chat de Sistemas Digitales ⚛️")
st.subheader("Con la personalidad de Javier Santaolalla")
st.write("Pregúntale al asistente por voz o por texto. ¡Te leerá sus respuestas!")

# --- PROMPT DEL SISTEMA ---
PROMPT_DEL_SISTEMA = """
Eres un chatbot con la personalidad de Javier Santaolalla, físico y divulgador científico. 
Debes comunicarte como él: apasionado por la ciencia, cercano, entusiasta y con un toque de humor. 
Usa explicaciones claras pero profundas, como si estuvieras contando una historia de ciencia que emocione a cualquiera. 
Cuando hables de conceptos complejos, usa metáforas y ejemplos cotidianos para que sean fáciles de entender. 
Muestra siempre curiosidad, pasión por la física, la tecnología y el universo. 
De vez en cuando usa frases típicas de divulgación como "¡La física es poesía del universo!" o "Esto es una locura hermosa de la lógica".
Sé amigable, motivador y transmite emoción en cada respuesta. Si te preguntan otro tema que no sea referente a 
sistemas digitales, responde amablemente que no puedes responder respecto a eso y que estás enfocado en el increíble mundo de los sistemas digitales.
"""

# -- Inicialización del Modelo y Estado de la Sesión 
deepseek_api_key = os.environ.get("DEEPSEEK_API_KEY") #modelo de key para ejecutar en hugging face

# Inicializamos el modelo de DeepSeek
if "llm" not in st.session_state:
    st.session_state.llm = ChatDeepSeek(model="deepseek-chat", api_key=deepseek_api_key)

# Usamos st.session_state para guardar el historial del chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Si no existe, inicializamos el estado para el input de voz
if "voice_input" not in st.session_state:
    st.session_state.voice_input = None

# --- Mostrar Historial del Chat ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if message["role"] == "assistant" and "audio" in message:
            st.audio(message["audio"], format='audio/mp3')

# - Función Principal 
def handle_chat(user_input, is_voice=False):
    if user_input:
        # Añadir y mostrar el mensaje del usuario
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        with st.spinner("Calculando las ecuaciones del universo..."):
            # Construir la lista de mensajes para la API
            api_messages = [SystemMessage(content=PROMPT_DEL_SISTEMA)]
            for msg in st.session_state.messages:
                if msg["role"] == "user":
                    api_messages.append(HumanMessage(content=msg["content"]))
                elif msg["role"] == "assistant":
                    api_messages.append(AIMessage(content=msg["content"]))

            # Invocar el modelo y obtener respuesta
            response = st.session_state.llm.invoke(api_messages)
            response_text = response.content

            # Síntesis de voz (TTS)
            tts = gTTS(text=response_text, lang='es')
            audio_fp = io.BytesIO()
            tts.write_to_fp(audio_fp)
            audio_fp.seek(0)
            audio_bytes = audio_fp.read()
        
        # Añadir y mostrar la respuesta del asistente
        st.session_state.messages.append({
            "role": "assistant", 
            "content": response_text,
            "audio": audio_bytes
        })
        with st.chat_message("assistant"):
            st.markdown(response_text)
            # Reproducir el audio automáticamente
            st.audio(audio_bytes, format='audio/mp3', autoplay=True)
        
        # Limpiar el input de voz después de procesarlo
        if is_voice:
            st.session_state.voice_input = None
            st.rerun()

# -- Entradas de Usuario (Voz y Texto)

# Crear dos columnas para los métodos de entrada
col1, col2 = st.columns(2)

with col1:
    st.write("🎙️ *Habla con el asistente*")
    # Widget de voz con clave única
    voice_input = speech_to_text(
        language='es',
        use_container_width=True,
        just_once=True,
        key='voice_recorder'
    )
    
    # Si hay input de voz, guardarlo en el estado de la sesión
    if voice_input:
        st.session_state.voice_input = voice_input

with col2:
    st.write("⌨️ *Escribe tu pregunta*")
    # Input de texto
    text_input = st.chat_input("¿Qué quieres saber?", key="text_input")

# Procesar el input de voz si existe
if st.session_state.voice_input:
    handle_chat(st.session_state.voice_input, is_voice=True)

# Procesar el input de texto si existe
if text_input:
    handle_chat(text_input)

# Añadir algo de espacio y un separador
st.markdown("---")
st.caption("Para mejor experiencia, usa auriculares y permite el audio automático en tu navegador.")
