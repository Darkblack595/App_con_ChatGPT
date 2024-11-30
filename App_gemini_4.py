import streamlit as st
import pandas as pd
import re
import io

# Intentar importar xlsxwriter y manejar el error si no está instalado
try:
    import xlsxwriter
except ImportError:
    import os
    os.system('pip install xlsxwriter')
    import xlsxwriter

# Título de la app
st.title("Premier League Stats Analyzer")
st.markdown("<h6>Hecha por Juan Pablo Gaviria Orozco</h6>", unsafe_allow_html=True)

# URL del archivo CSV de muestra (reemplaza con la URL real o carga un archivo local)
csv_url = 'https://datastore.premierleague.com/download/premier_league_stats.csv'

@st.cache_data
def cargar_datos(url):
    try:
        data = pd.read_csv(url)
        return data
    except Exception as e:
        st.error(f"Error al cargar los datos: {e}")
        return None

# Función para depurar y clasificar datos usando regex
def depurar_datos(data):
    maximos_goleadores = data.nlargest(5, 'Goals')[['Player Name', 'Goals']]
    maximos_asistidores = data.nlargest(5, 'Assists')[['Player Name', 'Assists']]
    equipos_campeones = data.groupby('Team')['Championships'].sum().nlargest(5).reset_index()
    equipos_subcampeones = data.groupby('Team')['Runner-ups'].sum().nlargest(5).reset_index()

    return maximos_goleadores, maximos_asistidores, equipos_campeones, equipos_subcampeones

# Convertir a Excel
def convertir_a_excel(data, sheet_name):
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        for df, name in zip(data, sheet_name):
            df.to_excel(writer, index=False, sheet_name=name)
            
            worksheet = writer.sheets[name]
            for i, col in enumerate(df.columns):
                max_len = df[col].astype(str).map(len).max()
                worksheet.set_column(i, i, max_len + 2)
    return output.getvalue()

# Cargar datos del CSV
data = cargar_datos(csv_url)

if data is not None:
    # Mostrar los datos cargados
    st.write("Datos del archivo CSV:")
    st.dataframe(data)

    # Depurar y clasificar datos
    maximos_goleadores, maximos_asistidores, equipos_campeones, equipos_subcampeones = depurar_datos(data)

    # Mostrar resultados
    st.write("Máximos Goleadores:")
    st.dataframe(maximos_goleadores)

    st.write("Máximos Asistidores:")
    st.dataframe(maximos_asistidores)

    st.write("Equipos Más Campeones:")
    st.dataframe(equipos_campeones)

    st.write("Equipos Más Subcampeones:")
    st.dataframe(equipos_subcampeones)

    # Botón para generar archivo .xls
    if st.button("Generar archivo .xls"):
        excel_data = convertir_a_excel(
            [maximos_goleadores, maximos_asistidores, equipos_campeones, equipos_subcampeones],
            ["Maximos Goleadores", "Maximos Asistidores", "Equipos Campeones", "Equipos Subcampeones"]
        )
        if excel_data:
            st.download_button(
                label="Descargar archivo .xls",
                data=excel_data,
                file_name='premier_league_stats.xlsx',
                mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            )
else:
    st.error("No se pudo cargar el archivo CSV. Por favor, verifica la URL o el formato del archivo.")
