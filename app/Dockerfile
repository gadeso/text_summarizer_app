# Utilizar una imagen base oficial de Python
FROM python:3.11-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el archivo requirements.txt y el código fuente al contenedor
COPY requirements.txt .
COPY api_model.py .
COPY database.py .
COPY templates/ ./templates/

# Instalar las dependencias
RUN pip install -r requirements.txt

# Configurar variables de entorno para la base de datos
ENV DATABASE_URL="mysql+mysqlconnector://admin:12345678@database-1.c9iyc4yeeeax.eu-north-1.rds.amazonaws.com:3306"

# Comando para ejecutar la aplicación
CMD ["uvicorn", "api_model:app", "--host", "0.0.0.0", "--port", "8000"]