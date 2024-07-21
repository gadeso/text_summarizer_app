## Proyecto de Resumen de Textos con Docker y AWS

Este proyecto proporciona una solución de resumen automático de textos utilizando un modelo preentrenado. Se ha dockerizado todo el entorno y se ha integrado con una base de datos de AWS para gestionar las entradas y resultados de los resúmenes. El componente principal del proyecto es el script api_model.py, que permite a los clientes interactuar con el servicio a través de una API.


#### Descripción del Proyecto

El objetivo principal de este proyecto es ofrecer un servicio de resumen de textos que:

- Utiliza un modelo preentrenado para generar resúmenes de texto.
- Dockeriza la aplicación para facilitar su despliegue en cualquier entorno.
- Conecta a una base de datos en AWS para almacenar y gestionar los textos y resúmenes.


#### Componentes del Proyecto

- api_model.py: Este es el script principal que expone la API para que los clientes puedan enviar textos y recibir resúmenes. Está implementado usando FastAPI para proporcionar una interfaz HTTP.

- Modelo LLM: Utiliza un modelo de resumen de texto previamente entrenado. El modelo se carga en la memoria al inicio de la aplicación para realizar inferencias rápidas.

- Docker: Se ha creado una imagen de Docker que encapsula toda la aplicación y sus dependencias, facilitando su ejecución en cualquier entorno compatible con Docker.

- Base de Datos AWS: La aplicación se conecta a una base de datos alojada en AWS para almacenar y recuperar textos y resúmenes. Se utiliza AWS RDS para la gestión de la base de datos relacional.


#### Cómo Empezar
Para ejecutar el proyecto en un entorno Dockerizado, te dejo el enlace del Docker Hub: https://hub.docker.com/repository/docker/gadesousaa/summarizer-app/general

Al ejecutar la imagen de Docker, podrás ingresar a la app a través de tu explorador favorito usando localhost:8000

Al estar en la interfaz, podrás ingresar textos en inglés o español y el modelo te regresará tu texto correctamente resumido


#### Contacto
Ante cualquier duda, recomendacion o incidente puedes contactarme a través de desousaga@gmail.com. ¡Muchas gracias!
