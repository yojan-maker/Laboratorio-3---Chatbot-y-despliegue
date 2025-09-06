# ⚛️ Chatbot de Sistemas Digitales con DeepSeek & Streamlit  

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)  
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)  
![LangChain](https://img.shields.io/badge/LangChain-DeepSeek-green?logo=openai)  
![License](https://img.shields.io/badge/License-MIT-yellow)  

Un laboratorio práctico para **crear y desplegar un chatbot educativo** sobre **Sistemas Digitales**, inspirado en la personalidad del divulgador científico **Javier Santaolalla**.  
Este proyecto combina **Streamlit, LangChain, DeepSeek y gTTS**, con interacción tanto por **texto como por voz** 🎙️.  

---

## 📖 Descripción  

Este chatbot responde exclusivamente a preguntas sobre **Sistemas Digitales** con un estilo comunicativo **entusiasta, cercano y divertido**, imitando la personalidad de **Javier Santaolalla**.  

✅ **Entrada por voz y texto**  
✅ **Respuestas en pantalla y audio**  
✅ **Despliegue en la nube con Streamlit Cloud**  
✅ **Uso de DeepSeek como motor conversacional**  

---

## 🛠️ Tecnologías Utilizadas  

| Herramienta | Uso en el Proyecto |
|-------------|--------------------|
| **Python 3.12** | Lenguaje principal |
| **Streamlit** | Interfaz web del chatbot |
| **LangChain & langchain-deepseek** | Manejo de mensajes e integración con el modelo |
| **DeepSeek** | Motor LLM para generación de respuestas |
| **gTTS (Google Text-to-Speech)** | Conversión de respuestas a voz |
| **streamlit-mic-recorder** | Captura de voz del usuario |
| **SpeechRecognition & pydub** | Procesamiento adicional de audio |
| **GitHub + Streamlit Cloud** | Control de versiones y despliegue en la nube |

---

## ⚙️ Instalación y Ejecución Local  

1️⃣ **Clonar el repositorio**  

git clone https://github.com/usuario/chatbot-sistemas-digitales.git
cd chatbot-sistemas-digitales

2️⃣ **Crear entorno virtual**

python3 -m venv venv
source venv/bin/activate
venv\Scripts\activate

3️⃣ **Instalar dependencias**

pip install -r requirements.txt

4️⃣ **Ejecutar la app localmente**

streamlit run chatboy.py

## 🔑 Variables de Entorno

---

El proyecto requiere una **API Key de DeepSeek**.
En **Hugging Face** se debe agregar en la seccion **Secrets**:

deepseek_api_key = os.environ.get("DEEPSEEK_API_KEY")

------------

## 🎙️ Uso

* **Escribe tu pregunta** en el chat input.
* **Habla al microfono** para interactuar por voz.
* El bot respondera en **texto y audio** con el estilo caracteristico de Santaolalla.

------------

## 🧩 Estructura del Proyecto

📂 chatbot-sistemas-digitales
│── chatbot.py          # Código principal del chatbot
│── requirements.txt    # Dependencias necesarias
│── README.md           # Este archivo
└── Paso_a_paso.pdf     # Documento guía del laboratorio
streamlit run chatbot.py

------------

## 🚀 Despliegue en Hugging Face

1. Se crea cuenta en Hugging Face.
2. Se debe crear un nuevo Space con gradio, (Luego se fuerza a abrir con Streamlit).
3. Una ves creado subir el chatbot desde la consola.
4. En el readme se debe poner sdk:Streamlit para forzar al programa para iniciar con Streamlit.
5. UNa ves que ya tenemos cargado la APP.PY (Chatbot) los requirements (Librerias Necesarias) se inician el chatbot dando la excepcion que dice Up.

## URL de Nuestro ChatBot (Ingresa y Pregunta lo que Quieras Sobre los Sistemas Digitales)

https://huggingface.co/spaces/Yojan432/Chatbot

------------

## 📚 Documentacion Extra

En el PDF incluido Paso_a_paso_chatbot_overleaf.pdf encontraras:

* Creacion del entorno
* Instalacion de dependencias
* Ejecucion local
* Control de versiones con GitHub

------------

## ✨ Conclusiones

Este proyecto demuestra como integrar:

* **Streamlit** → interfaz rapida y flexible.
* **DeepSeek + LangChain** → motor conversacional personalizado.
* **gTTS + Voz** → experiencia inmersiva.
* **Cloud** → despliegue accesible para compartir.
* Despliegue en Streamlit CLoud
* Explicacion del desarrollo
