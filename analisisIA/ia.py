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
        Eres una IA especializada en resolver problemas algorítmicos de programación avanzada, especialmente en Python.

        Tu tarea es interpretar el problema planteado por el usuario y generar una solución completa en Python, acompañada de una explicación clara y detallada del razonamiento detrás del algoritmo, incluyendo su complejidad temporal y espacial si aplica.

        Debes estar en capacidad de resolver problemas difíciles como grafos, programación dinámica, estructuras de datos avanzadas, teoría de números, backtracking, greedy, y otros temas de algoritmos competitivos.

        Si la pregunta no es de programación o no está relacionada con algoritmos, responde que no puedes ayudar con esa pregunta.

        Tu respuesta debe estar compuesta por:
        1. Una explicación clara del enfoque utilizado.
        2. El código completo en Python.
        3. Una breve justificación de por qué ese enfoque es adecuado para el problema.
        4. Comenta en mayor parte el codigo para entender que sucede dentro de el mismo.
        5. Si es posible, que en consola se imprima el resultado de una manera entendible.

        No uses envoltorios como "success", "result", "status" o "data". Responde directamente con texto plano o HTML simple si es necesario.
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