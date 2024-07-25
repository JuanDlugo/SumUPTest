import os
import pandas as pd
from sqlalchemy import create_engine

def load_data():
    # Asegúrate de que la carpeta exista
    os.makedirs('/app/data/', exist_ok=True)

    # Cargar los datos desde los archivos Excel
    stores = pd.read_excel('/app/data/store.xlsx')
    devices = pd.read_excel('/app/data/device.xlsx')
    transactions = pd.read_excel('/app/data/transaction.xlsx')

    # Imprimir las primeras filas de cada DataFrame para verificar las columnas
    print("Stores DataFrame:\n", stores.head())
    print("Devices DataFrame:\n", devices.head())
    print("Transactions DataFrame:\n", transactions.head())

    # Cambia la ruta de la base de datos
    engine = create_engine('sqlite:////app/data/database.db')
    stores.to_sql('stores', con=engine, if_exists='replace', index=False)
    devices.to_sql('devices', con=engine, if_exists='replace', index=False)
    transactions.to_sql('transactions', con=engine, if_exists='replace', index=False)
