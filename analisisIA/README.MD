
## 🧠 Proyecto: Resolución de Problemas Algorítmicos con Gemini API

Este proyecto utiliza la API de Gemini (Google Generative AI) para resolver problemas complejos de programación en Python.
La IA interpreta preguntas algorítmicas, genera código funcional y explica el razonamiento detrás de la solución.

---

### ⚙️ Requisitos Previos

* Python 3.8 o superior
* Clave de API de Gemini: [https://makersuite.google.com/app](https://makersuite.google.com/app)

---

### 🧪 Instalación y Ejecución

1. **Clona o crea la estructura del proyecto.**

2. **Crea un entorno virtual:**

   ```bash
   python -m venv venv
   ```

3. **Activa el entorno virtual:**

   * Windows CMD:

     ```bash
     venv\Scripts\activate
     ```

4. **Instala las dependencias:**

   ```bash
   pip install python-dotenv google-generativeai
   ```

   > 💡 Si quieres mantener un archivo de dependencias, puedes usar `requirements.txt`.

5. **Agrega tu clave de API en el archivo `.env`:**

   ```
   GEMINI_API_KEY=tu_clave_aqui
   ```

6. **Escribe tu reto en un archivo dentro de la carpeta `problemas/`. Ejemplo:**

   ```
   problemas/reto1.txt
   problemas/reto2.txt
   ```

7. **Ejecuta el proyecto:**

   ```bash
   python main.py
   ```

---

### 🧩 ¿Qué hace el proyecto?

#### 1. `main.py`

* Lee el contenido de un archivo de `problemas/` (ej: `reto1.txt`).
* Llama a `api_ia(query)` desde `ia.py`.
* Imprime en consola la respuesta generada por la IA (explicación + código).

#### 2. `ia.py`

* Carga la clave de API desde `.env`.
* Configura el modelo `gemini-2.5-flash-lite`.
* Define un prompt especializado para resolver problemas algorítmicos.
* Envía la pregunta a Gemini y devuelve la respuesta en texto plano.

---

## 📌 El reto del estudiante

El estudiante debe escribir un **prompt claro** en cada archivo de la carpeta `problemas/`.
Ese prompt debe guiar a la IA para que genere un resultado estructurado.

La salida **debe contener obligatoriamente**:

1. Explicación clara del enfoque utilizado.
2. Código completo en Python (funcional y comentado).
3. Justificación breve del enfoque elegido (complejidad y comparación si aplica).
4. Ejemplo de ejecución en consola con un resultado entendible.
5. Comentarios dentro del código que refuercen la explicación.

Además, cada **prompt utilizado** debe guardarse en la carpeta:

```

prompts/

```

Por ejemplo:

```

prompts/reto1_prompt.txt
prompts/reto2_prompt.txt

```

Esto asegura que el alumno entregue tanto el **problema original** (en `problemas/`) como el **prompt diseñado** para resolverlo (en `prompts/`).

---

📌 **Importante:**
La IA **no debe devolver formatos extraños** como `success`, `result`, `status` o JSON.
La respuesta debe ser únicamente en **texto plano** o **Python comentado**.

---

### 📝 Ejemplo de cómo escribir un reto (`problemas/reto1.txt`)

Resuelve el siguiente problema algorítmico en Python:

Dado un grafo dirigido con n nodos y m aristas, implementa un algoritmo que detecte si existe un ciclo. Explica el enfoque, muestra el código en Python con comentarios, justifica por qué ese enfoque es adecuado y ejecuta un ejemplo en consola con el resultado.

Tu respuesta debe estar compuesta por:
1. Una explicación clara del enfoque utilizado.
2. El código completo en Python.
3. Una breve justificación de por qué ese enfoque es adecuado para el problema.
4. Si es posible, que en consola se imprima el resultado de una manera entendible.
5. Todos los puntos anteriores deben de estar comentados dentro del mismo código para un mayor entendimiento del programa.

No uses envoltorios como "success", "result", "status" o "data". Responde directamente en texto plano.