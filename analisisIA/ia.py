# 📦 Importa módulos necesarios para configuración y conexión con la API
import os
from dotenv import load_dotenv                      # Para cargar variables de entorno desde un archivo .env
from google.generativeai import configure, GenerativeModel  # SDK oficial para interactuar con Gemini

# ✅ Cargar variables de entorno desde el archivo .env
# Esto permite acceder a la clave de API sin exponerla directamente en el código
load_dotenv()

# 🔐 Configura la API de Gemini usando la clave almacenada en la variable de entorno GEMINI_API_KEY
configure(api_key=os.getenv("GEMINI_API_KEY"))

# ✅ Inicializa el modelo específico de Gemini que se va a usar
# "gemini-2.5-flash-lite" es una versión rápida y eficiente, ideal para respuestas ágiles
model = GenerativeModel(model_name="gemini-2.5-flash-lite")

# 🧠 Función principal que envía una pregunta a la IA y devuelve la respuesta
def api_ia(query):
    try:
        # 📝 Prompt especializado que define el comportamiento deseado de la IA
        # Le indica que debe resolver problemas algorítmicos en Python, explicar el razonamiento,
        # comentar el código y mostrar resultados entendibles en consola
        prompt = """

        Aqui es donde debes poner el prompt especializado para que la IA resuelva los retos. Suerte!

        """.strip()

        # 🚀 Envía el prompt + la pregunta del usuario al modelo Gemini
        # La IA genera una respuesta basada en el contexto y las instrucciones del prompt
        response = model.generate_content(f"{prompt}\n\nAcción:\n{query}")

        # 🧾 Extrae el texto plano de la respuesta generada por la IA
        response_text = response.text.strip()

        # ✅ Devuelve la respuesta final al llamador (por ejemplo, main.py)
        return response_text

    # ⚠️ Manejo de errores si ocurre algún problema durante la conexión o generación
    except Exception as e:
        print("❌ Error en la API de Gemini:", str(e))
        return {
            "type": "error",
            "data": "Error al procesar la pregunta con la IA.",
            "error": str(e),
        }