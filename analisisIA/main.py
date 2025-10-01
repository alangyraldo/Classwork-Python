# 📦 Importa la función principal que conecta con la IA desde el módulo ia_service.py
# Este archivo debe contener la función api_ia(query)
from ia import api_ia

# ✅ Abre el archivo que contiene la pregunta a resolver
# En este caso, se accede a datos/problema1.txt, que debe contener una pregunta algorítmica en texto plano
# El modo "r" indica modo lectura, y encoding="utf-8" asegura compatibilidad con caracteres especiales
with open("datos/reto1.txt", "r", encoding="utf-8") as f:
    # Lee todo el contenido del archivo y elimina espacios en blanco al inicio y final
    pregunta = f.read().strip()

# 🚀 Llama a la función api_ia con la pregunta como argumento
# Esta función se encarga de enviar el texto a la API de Gemini, aplicar el prompt especializado,
# recibir la respuesta, procesarla (como texto plano o JSON) y devolverla
resultado = api_ia(pregunta)

# 📤 Muestra en consola el resultado generado por la IA
# Puede ser una explicación + código en Python, o un error si algo falló
print("📤 Resultado final:", resultado)
