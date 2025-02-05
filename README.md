# ❔ QnAProject

## 🖋️ Descripción

Este proyecto es una aplicación interactiva de preguntas y respuestas (QnA) construida con **Streamlit** que permite a los usuarios obtener respuestas sobre la familia de consolas **Nintendo 3DS** y los juegos **Mario Kart 7** y **Animal Crossing: New Leaf**. La app utiliza **Azure Language Studio** para generar respuestas basadas en una base de conocimiento previamente configurada, ofreciendo también sugerencias para preguntas de seguimiento.

## 💪 Características

- Interfaz intuitiva para preguntar y recibir respuestas.
- Sugerencias de preguntas para explorar temas relacionados.
- Interacción con la base de conocimiento de Azure Language Studio.
- Posibilidad de obtener información de fuentes externas como las _wikis_ utilizadas.

## 🔧 Tecnologías Utilizadas

- Streamlit: Framework para crear la interfaz web interactiva.
- Azure Language Studio: API para responder preguntas a partir de una base de conocimiento.
- Python: Lenguaje de programación utilizado para la lógica de la aplicación.
- dotenv: Gestión de variables de entorno (como las credenciales de Azure).

## ⬇️ Instalación

Clona este repositorio:

```bash
git clone https://github.com/alejandrorod-tajamar/QnAProject.git
```

Navega al directorio del proyecto:

```cmd
cd QnAProject
```

Crea un entorno virtual:

```cmd
python -m venv .venv
```

Activa el entorno virtual:

```cmd
.\.venv\Scripts\activate
```

Instala las dependencias:

```cmd
pip install -r requirements.txt
```

Configura las credenciales de Azure: Crea un archivo `.env` en la raíz del proyecto con las siguientes variables de entorno:

```ini
AI_SERVICE_ENDPOINT=tu_endpoint_azure
AI_SERVICE_KEY=tu_clave_azure
QA_PROJECT_NAME=tu_nombre_proyecto_qa
QA_DEPLOYMENT_NAME=tu_nombre_despliegue_qa
```

Ejecuta la aplicación:

```cmd
streamlit run app.py
```

La aplicación estará disponible en `http://localhost:8501`.
