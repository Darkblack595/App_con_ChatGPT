# streamlit_app.py

import pandas as pd
import streamlit as st
from io import StringIO

# Función para calcular los tiempos promedio de entrega
def calcular_tiempos_entrega(data):
    data['Fecha_Entrega'] = pd.to_datetime(data['Fecha_Entrega'], errors='coerce')
    data['Fecha_Pedido'] = pd.to_datetime(data['Fecha_Pedido'])
    data['Tiempo_Entrega'] = (data['Fecha_Entrega'] - data['Fecha_Pedido']).dt.days
    tiempo_promedio_entrega = data['Tiempo_Entrega'].mean(skipna=True)
    return tiempo_promedio_entrega

# Configuración de la aplicación
st.title("Seguimiento de Pedidos de Ecommerce")

# Cargar URl
url = "https://raw.githubusercontent.com/gabrielawad/programacion-para-ingenieria/refs/heads/main/archivos-datos/pandas/pedidos_ecommerce.csv"
# Subir archivo CSV
uploaded_file = pd.read_csv(url, sep=",", header=0)

if uploaded_file is not None:
    # Cargar datos
    data = pd.read_csv(uploaded_file)

    # Mostrar los datos cargados
    st.write("Datos Cargados:")
    st.dataframe(data.head())

    # Filtrar pedidos por estado
    estado_seleccionado = st.selectbox("Selecciona el estado del pedido", options=["Todos", "Pendiente", "Enviado", "Entregado"])
    if estado_seleccionado != "Todos":
        data = data[data['Estado'] == estado_seleccionado]

    # Mostrar datos filtrados
    st.write(f"Pedidos en estado: {estado_seleccionado}")
    st.dataframe(data)

    # Calcular y mostrar el tiempo promedio de entrega
    tiempo_promedio = calcular_tiempos_entrega(data)
    st.write(f"Tiempo promedio de entrega: {tiempo_promedio:.2f} días")

    # Generar informe descargable
    csv = data.to_csv(index=False)
    st.download_button(
        label="Descargar informe",
        data=csv,
        file_name='informe_pedidos.csv',
        mime='text/csv',
    )
