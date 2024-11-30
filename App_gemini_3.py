import streamlit as st
import pandas as pd
import requests
import io
from datetime import datetime

# Intentar importar xlsxwriter y manejar el error si no está instalado
try:
    import xlsxwriter
except ImportError:
    st.error("El módulo xlsxwriter no está instalado. Por favor, instálalo ejecutando `pip install xlsxwriter`.")

# Título de la app
st.title("Generador de Archivos .xls")
st.markdown("<h6>Hecha por Juan Pablo Gaviria Orozco</h6>", unsafe_allow_html=True)

# URL del archivo CSV en GitHub
csv_url = 'https://github.com/gabrielawad/programacion-para-ingenieria/blob/4833a91f25a8154042cfb5e51835f7719f4679be/archivos-datos/regex/regex_productos.csv'

@st.cache
def cargar_datos(url):
    download = requests.get(url).content
    data = pd.read_csv(io.StringIO(download.decode('utf-8')))
    return data

# Cargar datos del CSV
data = cargar_datos(csv_url)

# Mostrar los datos cargados
st.write("Datos del archivo CSV:")
st.dataframe(data)

# Convertir a Excel
def convertir_a_excel(data):
    output = io.BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    data.to_excel(writer, index=False, sheet_name='Sheet1')

    workbook = writer.book
    worksheet = writer.sheets['Sheet1']

    # Formateo de columnas
    worksheet.set_column('A:A', 20)
    worksheet.set_column('B:B', 30)
    worksheet.set_column('C:C', 15)
    worksheet.set_column('D:D', 20)
    worksheet.set_column('E:E', 40)

    writer.save()
    processed_data = output.getvalue()
    return processed_data

# Botón para generar archivo .xls
if st.button("Generar archivo .xls") and 'xlsxwriter' in globals():
    excel_data = convertir_a_excel(data)
    st.download_button(
        label="Descargar archivo .xls",
        data=excel_data,
        file_name='productos.xlsx',
        mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )

    # Vista previa del archivo generado
    st.write("Vista previa del archivo generado:")
    st.dataframe(data)
