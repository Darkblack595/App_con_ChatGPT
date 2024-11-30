import streamlit as st
import pandas as pd
import os
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

# Carpeta de datos
data_folder = 'https://github.com/Darkblack595/App_con_ChatGPT/tree/7f2d53bbddcf0920e9cf1eec921355e333d7a083/Premier_Data'

# Función para cargar datos
def cargar_datos():
    all_data = []
    for season_file in os.listdir(data_folder):
        if season_file.endswith('leaguetable.csv'):
            season_data = pd.read_csv(os.path.join(data_folder, season_file))
            season_data['Season'] = season_file.split('epl')[1].split('leaguetable')[0]
            all_data.append(season_data)
    return pd.concat(all_data)

# Función para depurar y clasificar datos
def depurar_datos(data):
    equipos_campeones = data[data['position'] == 1]
    equipos_subcampeones = data[data['position'] == 2]

    return equipos_campeones, equipos_subcampeones

# Función para análisis de estadísticas
def estadisticas_generales(data):
    total_goles_anotados = data['goalsscored'].sum()
    total_goles_concedidos = data['goalsconceded'].sum()
    equipos_mas_goleadores = data.groupby('club')['goalsscored'].sum().nlargest(5).reset_index()
    equipos_mas_goleados = data.groupby('club')['goalsconceded'].sum().nlargest(5).reset_index()

    return total_goles_anotados, total_goles_concedidos, equipos_mas_goleadores, equipos_mas_goleados

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
data = cargar_datos()

if data is not None:
    # Mostrar los datos cargados
    st.write("Datos de la Premier League:")
    st.dataframe(data)

    # Depurar y clasificar datos
    equipos_campeones, equipos_subcampeones = depurar_datos(data)
    
    # Análisis de estadísticas generales
    total_goles_anotados, total_goles_concedidos, equipos_mas_goleadores, equipos_mas_goleados = estadisticas_generales(data)

    # Mostrar resultados
    st.write("Equipos Campeones por Temporada:")
    st.dataframe(equipos_campeones)

    st.write("Equipos Subcampeones por Temporada:")
    st.dataframe(equipos_subcampeones)
    
    st.write("Estadísticas Generales:")
    st.write(f"Total de Goles Anotados: {total_goles_anotados}")
    st.write(f"Total de Goles Concedidos: {total_goles_concedidos}")
    
    st.write("Equipos Más Goleadores:")
    st.dataframe(equipos_mas_goleadores)

    st.write("Equipos Más Goleados:")
    st.dataframe(equipos_mas_goleados)

    # Botón para generar archivo .xls
    if st.button("Generar archivo .xls"):
        excel_data = convertir_a_excel(
            [equipos_campeones, equipos_subcampeones, equipos_mas_goleadores, equipos_mas_goleados],
            ["Equipos Campeones", "Equipos Subcampeones", "Equipos Más Goleadores", "Equipos Más Goleados"]
        )
        if excel_data:
            st.download_button(
                label="Descargar archivo .xls",
                data=excel_data,
                file_name='premier_league_stats.xlsx',
                mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            )
else:
    st.error("No se pudo cargar los datos. Por favor, verifica la URL o el formato de los archivos.")
