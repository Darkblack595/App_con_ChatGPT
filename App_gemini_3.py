import streamlit as st
import pandas as pd
import requests
import io
import re
from datetime import datetime

# Intentar importar xlsxwriter y manejar el error si no está instalado
try:
    import xlsxwriter
except ImportError:
    import os
    os.system('pip install xlsxwriter')
    import xlsxwriter

# Título de la app
st.title("Generador de Archivos .xls")
st.markdown("<h6>Hecha por Juan Pablo Gaviria Orozco</h6>", unsafe_allow_html=True)

# URL del archivo CSV en GitHub
csv_url = 'https://raw.githubusercontent.com/gabrielawad/programacion-para-ingenieria/4833a91f25a8154042cfb5e51835f7719f4679be/archivos-datos/regex/regex_productos.csv'

@st.cache_data
def cargar_datos(url):
    try:
        download = requests.get(url).content
        data = pd.read_csv(io.StringIO(download.decode('utf-8')), header=None)
        return data
    except Exception as e:
        st.error(f"Error al cargar los datos: {e}")
        return None

# Función para depurar y clasificar datos usando regex
def depurar_datos(data):
    series = []
    nombres = []
    valores = []
    fechas = []
    contactos = []

    for index, row in data.iterrows():
        text = row[0]  # Asumimos que los datos están en la primera columna

        # Número de serie del producto
        serie = re.search(r"Serie:\s*([A-Za-z0-9]+)", text)
        series.append(serie.group(1) if serie else "")

        # Nombre del producto
        nombre = re.search(r"Nombre:\s*([A-Za-z\s]+)", text)
        nombres.append(nombre.group(1) if nombre else "")

        # Valor del producto
        valor = re.search(r"Valor:\s*([0-9]+\.[0-9]{2})", text)
        valores.append(valor.group(1) if valor else "")

        # Fecha de compra del producto
        fecha = re.search(r"Fecha:\s*([0-9]{2}/[0-9]{2}/[0-9]{2})", text)
        fechas.append(fecha.group(1) if fecha else "")

        # Información de contacto
        contacto = re.search(r"Contacto:\s*([A-Za-z0-9@\.]+)", text)
        contactos.append(contacto.group(1) if contacto else "")

    depurado_data = pd.DataFrame({
        "Número de Serie": series,
        "Nombre del Producto": nombres,
        "Valor": valores,
        "Fecha de Compra": fechas,
        "Contacto": contactos
    })

    return depurado_data

# Convertir a Excel
def convertir_a_excel(data):
    output = io.BytesIO()
    try:
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            data.to_excel(writer, index=False, sheet_name='Sheet1')

            workbook = writer.book
            worksheet = writer.sheets['Sheet1']

            # Formateo de columnas
            worksheet.set_column('A:A', 20)
            worksheet.set_column('B:B', 30)
            worksheet.set_column('C:C', 15)
            worksheet.set_column('D:D', 20)
            worksheet.set_column('E:E', 40)

        processed_data = output.getvalue()
        return processed_data
    except Exception as e:
        st.error(f"Error al convertir a Excel: {e}")
        return None

# Cargar datos del CSV
data = cargar_datos(csv_url)

if data is not None:
    # Mostrar los datos cargados
    st.write("Datos del archivo CSV:")
    st.dataframe(data)

    # Depurar y clasificar datos
    datos_depurados = depurar_datos(data)

    # Botón para generar archivo .xls
    if st.button("Generar archivo .xls"):
        excel_data = convertir_a_excel(datos_depurados)
        if excel_data:
            st.download_button(
                label="Descargar archivo .xls",
                data=excel_data,
                file_name='productos.xlsx',
                mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            )

            # Vista previa del archivo generado
            st.write("Vista previa del archivo generado:")
            st.dataframe(datos_depurados)
else:
    st.error("No se pudo cargar el archivo CSV. Por favor, verifica la URL o el formato del archivo.")
