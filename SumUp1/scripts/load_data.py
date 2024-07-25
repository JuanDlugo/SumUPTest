import pandas as pd
from sqlalchemy import create_engine

print('ENTRE EN LOAD DATA PY')
# Leer los archivos Excel
stores = pd.read_excel('/app/scripts/data/store.xlsx')
devices = pd.read_excel('/app/scripts/data/device.xlsx')
transactions = pd.read_excel('/app/scripts/data/transaction.xlsx')


print('ECargados los archivos Excel')
# Conectar a MySQL
engine = create_engine('mysql+pymysql://dbt_user:password@db:3306/SumUpTest1')



print('ENGINE')
# Cargar los datos en MySQL
stores.to_sql('stores', con=engine, if_exists='replace', index=False)
devices.to_sql('devices', con=engine, if_exists='replace', index=False)
transactions.to_sql('transactions', con=engine, if_exists='replace', index=False)



print('Termine de cargar los datos en MySQL')