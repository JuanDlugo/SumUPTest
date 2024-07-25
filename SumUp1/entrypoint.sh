#!/bin/bash

# Esperar a que MySQL esté listo
while ! nc -z db 3306; do
  echo "Waiting for MySQL to start..."
  sleep 1
done

echo "MySQL started"

# Ejecutar el script de carga de datos
python /app/scripts/load_data.py
echo "Python ended" 

# Ejecutar dbt run
dbt run --profiles-dir /app/dbt_project --project-dir /app/dbt_project
