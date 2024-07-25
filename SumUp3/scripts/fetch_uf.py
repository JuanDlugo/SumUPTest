import requests
import pandas as pd
from sqlalchemy import create_engine, text
from bs4 import BeautifulSoup
from datetime import datetime

def fetch_and_store_uf():
    url = "https://si3.bcentral.cl/siete/ES/Siete/Cuadro/CAP_PRECIOS/MN_CAP_PRECIOS/UF_IVP_DIARIO"

    # Hacer la solicitud a la página web
    response = requests.get(url)
    content = response.text

    # Verificar el código de estado
    if response.status_code != 200:
        raise Exception(f"Failed to load page with status code {response.status_code}")

    # Parsear el contenido HTML
    soup = BeautifulSoup(content, 'html.parser')

    # Encontrar el div que contiene la información relevante
    div_wrapper = soup.find('div', class_='wrapper d-flex align-items-stretch', style='overflow-x: hidden;')

    if not div_wrapper:
        raise Exception("No se encontró el div con la clase especificada.")

    # Encontrar el div que contiene la tabla de datos
    div_content = div_wrapper.find('div', id='divCont')

    if not div_content:
        raise Exception("No se encontró el div con el id especificado.")

    # Encontrar la tabla de datos
    table = div_content.find('table', id='grilla')

    if not table:
        raise Exception("No se encontró la tabla con el id especificado.")

    # Extraer los encabezados de la tabla
    headers = [th.text.strip() for th in table.find_all('th')]

    # Extraer los datos de la tabla
    rows = table.find('tbody').find_all('tr')
    data = []
    for row in rows:
        cols = row.find_all('td')
        data.append([ele.text.strip() for ele in cols])

    # Crear un DataFrame de Pandas con los datos extraídos
    df = pd.DataFrame(data, columns=headers)

    # Filtrar solo la serie "Unidad de fomento (UF)"
    df_uf = df[df['Serie'] == 'Unidad de fomento (UF)']

    # Hacer copias para cada paso
    df_uf_values = df_uf.iloc[:, 2:].copy()

    # Eliminar los delimitadores de miles (puntos) y reemplazar comas por puntos
    df_uf_values = df_uf_values.apply(lambda x: x.str.replace('.', '').str.replace(',', '.') if x.dtype == "object" else x)

    # Convertir los valores de UF a float
    df_uf_values = df_uf_values.apply(pd.to_numeric, errors='coerce')

    # Transponer el DataFrame para tener una columna de fechas y una columna de valores
    df_uf_values = df_uf_values.transpose().reset_index()
    df_uf_values.columns = ['fecha', 'valor']

    # Guardar los datos en una base de datos usando SQLAlchemy
    engine = create_engine('sqlite:////app/data/database.db')
    df_uf_values.to_sql('uf_values', con=engine, if_exists='replace', index=False)

    # Obtener la fecha y el valor de la UF de hoy
    today = datetime.today().strftime('%d.%b.%Y')
    uf_today_row = df_uf_values[df_uf_values['fecha'] == today]
    if not uf_today_row.empty:
        uf_today = uf_today_row['valor'].values[0]
        print(f"La UF de hoy ({today}) es {uf_today}")
    else:
        print(f"No se encontró la UF para la fecha de hoy ({today})")

    # Imprimir la última fecha guardada
    print(f"Se guardó en la BDD la UF hasta el día {df_uf_values['fecha'].iloc[-1]}")

