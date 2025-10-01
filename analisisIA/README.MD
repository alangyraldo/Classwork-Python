## 🧠 Proyecto: Resolución de Problemas Algorítmicos con Gemini API

Este proyecto utiliza la API de Gemini (Google Generative AI) para resolver problemas complejos de programación en Python. La IA interpreta preguntas algorítmicas, genera código funcional y explica el razonamiento detrás de la solución.

---

### ⚙️ Requisitos Previos

- Python 3.8+
- Clave de API de Gemini: [https://makersuite.google.com/app](https://makersuite.google.com/app)

---

### 🧪 Instalación y Ejecución

1. **Crear la estructura del proyecto.**

2. **Crea un entorno virtual:**

   ```bash
   python -m venv venv
   ```

3. **Activa el entorno virtual:**

   - Windows CMD:
     ```bash
     venv\Scripts\activate
     ```

Perfecto, Adrián. Aquí tienes el paso corregido y ampliado para el archivo `README.md`, con la instalación directa de dependencias primero, y luego la opción de usar `requirements.txt` como alternativa:

---

### 4. **Instala las dependencias**

Ejecuta el siguiente comando para instalar las dependencias necesarias:

```bash
pip install python-dotenv google-generativeai
```

> 💡 **Opcional:** Si prefieres mantener un archivo de dependencias reproducible, puedes usar `requirements.txt`:

```bash
pip freeze > requirements.txt
```

Y para instalar las dependencias con el `requirements.txt`:

```bash
pip install -r requirements.txt
```

5. **Agrega tu clave de API en el archivo `.env`:**

   ```
   GEMINI_API_KEY=tu_clave_aquí
   ```

6. **Escribe una pregunta en `datos/problema.txt`. Ejemplo:**

   ```
   Dado un grafo dirigido, implementa una función en Python que detecte si hay ciclos. Explica el algoritmo usado y su complejidad.
   ```

7. **Ejecuta el proyecto:**
   ```bash
   python main.py
   ```

---

### 🧩 ¿Qué hace el proyecto?

#### 1. `main.py`

- Lee el contenido de `datos/problema.txt`.
- Llama a `api_ia(query)` desde `ia_service.py`.
- Imprime en consola la respuesta generada por la IA (explicación + código).

#### 2. `ia_service.py`

- Carga la clave de API desde `.env`.
- Configura el modelo `gemini-2.5-flash-lite`.
- Define un prompt especializado para resolver problemas algorítmicos.
- Envía la pregunta a Gemini.
- Procesa la respuesta:
  - Si contiene JSON válido, lo imprime.
  - Si no, muestra el texto plano con explicación y código.

---

### 🧠 Prompt personalizado

El prompt está diseñado para exigir a la IA:

- Resolver problemas complejos (grafos, DP, backtracking, etc.).
- Usar Python exclusivamente.
- Explicar el razonamiento detrás del algoritmo.
- Justificar la elección del enfoque.
- Rechazar preguntas que no sean de programación.

---

### 🧪 Ejercicios recomendados para probar la IA

Coloca cualquiera de estos en `datos/problema.txt`:

- Detección de ciclos en grafos dirigidos.
- Subconjunto con suma objetivo (DP).
- Problema de las N reinas (backtracking).
- Segment Tree para rango mínimo.
- Criba de Eratóstenes (teoría de números).
- Interval Scheduling (greedy).
- Camino más corto en laberinto (BFS).

---

### ✅ Resultado esperado

La IA debe responder con:

- ✅ Explicación clara del algoritmo.
- ✅ Código funcional en Python.
- ✅ Justificación del enfoque y complejidad.
