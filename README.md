# ❔ QnAProject

## 🖋️ Descripción

Este proyecto es una aplicación interactiva de preguntas y respuestas (QnA) construida con **Streamlit** que permite a los usuarios obtener respuestas sobre la familia de consolas **Nintendo 3DS** y los juegos **Mario Kart 7** y **Animal Crossing: New Leaf**. La app utiliza **Azure Language Studio** para generar respuestas basadas en una base de conocimiento previamente configurada, ofreciendo también sugerencias para preguntas de seguimiento.

## 💪 Características

- Base de conocimiento de Language Studio con más de 200 preguntas posibles.
- Respuestas con imágenes, tablas, iconos y enlaces.
- Interfaz intuitiva para preguntar y recibir respuestas.
- Sugerencias de preguntas para explorar temas relacionados.
- Posibilidad de obtener información de fuentes externas como las _wikis_ utilizadas.

## 🔧 Tecnologías Utilizadas

- Streamlit: Framework para crear la interfaz web interactiva.
- Azure Language Studio: API para responder preguntas a partir de una base de conocimiento.
- Python: Lenguaje de programación utilizado para la lógica de la aplicación.
- dotenv: Gestión de variables de entorno (como las credenciales de Azure).

## 📥 Acceso a la Aplicación

¡La aplicación ya está desplegada y puedes probarla en línea! Solo necesitas acceder al siguiente enlace:

[Nintendo 3DS QnA](https://alejandrorod-tajamar-qnaproject-app-m1eziw.streamlit.app/)

## 📲 Instrucciones de uso

1️⃣ Abre la aplicación en tu navegador.

2️⃣ En la barra lateral, puedes elegir algunas preguntas de ejemplo para probar la aplicación, o consultar las fuentes que utiliza.

3️⃣ Ingresa tu propia pregunta sobre Nintendo 3DS, Mario Kart 7, o Animal Crossing: New Leaf en el campo de texto y recibe la mejor respuesta. Si el servicio ofrece sugerencias sobre preguntas relacionadas, también aparecerán como botones para que las uses fácilmente.

🪧 ADVERTENCIA: La aplicación y el recurso están en `inglés`, por tanto, este será el idioma con el que se podrá interactuar con el chatbot.

💡 EJEMPLOS DE USO:

  1. Utilizar las preguntas sugeridas para obtener información sobre los personajes especiales de Animal Crossing:

     ![imagen](https://github.com/user-attachments/assets/cc41e2d6-322c-4571-8866-feae5d078676)
     
     ![imagen](https://github.com/user-attachments/assets/d886024f-8df3-4343-8864-1130f4e803db)
     
     ![imagen](https://github.com/user-attachments/assets/d29eecab-c5b2-4648-912b-948c948dcc5a)
     
     ![imagen](https://github.com/user-attachments/assets/8155a413-04d4-4ffa-b723-4b6e215189b9)
     
     ![imagen](https://github.com/user-attachments/assets/5c526845-8cd8-4a62-b2e0-1a19649907aa)
     
     ![imagen](https://github.com/user-attachments/assets/075343b2-2f7d-4666-a881-d7c8fca63e22)

  2. Utilizar las preguntas sugeridas para obtener información sobre las ruedas disponibles en Mario Kart:

     ![imagen](https://github.com/user-attachments/assets/bf8c033b-6551-464f-b03d-41b00dbb56cf)

     ![imagen](https://github.com/user-attachments/assets/aabe9f85-34c5-497d-b748-cbde87adbf73)

     ![imagen](https://github.com/user-attachments/assets/368a0148-95d5-4f04-9878-ad40dab45315)

     ![imagen](https://github.com/user-attachments/assets/446399f1-2a1d-44e4-93bb-04477dbf20c4)

     ![imagen](https://github.com/user-attachments/assets/5609c2cf-5646-4a8d-9671-ed85945c9358)

     ![imagen](https://github.com/user-attachments/assets/1bde1eda-84d6-42ae-810e-b8153189bcbb)

## ⬇️ Instalación (Opcional para usar otro recurso de Language Services)

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
