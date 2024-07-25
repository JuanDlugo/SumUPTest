# SumUpTest1 DBT Project

## Prerequisitos

1. Docker
2. Git

## Configuración del Proyecto

### 1. Clonar el repositorio

git clone <URL_DEL_REPOSITORIO>
cd SUMUP1

### 2. Construir y levantar los contenedores

docker-compose up --build

(El comando anterior generar tanto la BDD MySQL como el modelo de Datos DBT, migra y puebla las tablas en base a los archivos .xlsx que estan en scripts/data)

### 3. Ingresar a MySQL
Una vez que los contenedores estén levantados, debes abrir una nueva terminar y puedes ingresar a MySQL con el siguiente comando:

docker-compose exec db /bin/bash\
mysql -u dbt_user -ppassword SumUpTest1


### 4. 4. Ejecutar las consultas en MySQL
Dentro de la consola de MySQL, ejecuta las siguientes consultas para obtener los resultados de los modelos:

Top 10 Stores per Transacted Amount\
SELECT * FROM top_10_stores;


Top 10 Products Sold\
SELECT * FROM top_10_products;


Average Transacted Amount per Store Typology and Country\
SELECT * FROM avg_transacted_amount;


Percentage of Transactions per Device Type\
SELECT * FROM pct_transactions_device_type;


Average Time for a Store to Perform its First 5 Transactions\
SELECT * FROM avg_time_first_5_transactions;