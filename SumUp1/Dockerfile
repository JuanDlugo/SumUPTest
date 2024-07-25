# Utilizar una imagen base de Python
FROM python:3.8-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar los archivos de requisitos y el script de carga de datos
COPY requirements.txt requirements.txt
COPY scripts/ scripts/
COPY dbt_project/ dbt_project/
COPY entrypoint.sh /app/

# Instalar las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Instalar dbt y MySQL client
RUN pip install dbt-core dbt-mysql \
    && apt-get update \
    && apt-get install -y default-mysql-client netcat-openbsd git \
    && chmod +x /app/entrypoint.sh

# Comando por defecto para mantener el contenedor en ejecución
CMD ["/app/entrypoint.sh"]
