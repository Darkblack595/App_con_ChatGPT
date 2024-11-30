import streamlit as st
import re
import requests
import pandas as pd

# Título de la app
st.title("Recipe Finder")
st.markdown("<h6>Hecha por Juan Pablo Gaviria Orozco</h6>", unsafe_allow_html=True)

# URL de la API con datos de recetas
api_url = 'https://dummyjson.com/recipes'

@st.cache_data
def cargar_datos(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        json_data = response.json()
        return json_data['recipes']
    except Exception as e:
        st.error(f"Error al cargar los datos: {e}")
        return None

# Función para buscar recetas por ingredientes
def buscar_por_ingredientes(recetas, ingredientes):
    resultados = []
    for receta in recetas:
        if all(ing.lower() in receta['ingredients'].lower() for ing in ingredientes):
            resultados.append(receta)
    return resultados

# Función para buscar recetas por tiempo de preparación
def buscar_por_tiempo(recetas, tiempo):
    resultados = []
    for receta in recetas:
        if 'prepTime' in receta and int(receta['prepTime']) <= tiempo:
            resultados.append(receta)
    return resultados

# Función para buscar recetas por tipo de plato
def buscar_por_tipo(recetas, tipo):
    resultados = [receta for receta in recetas if tipo.lower() in receta['type'].lower()]
    return resultados

# Cargar datos de la API
recetas = cargar_datos(api_url)

if recetas:
    st.write("Datos cargados con éxito!")

    # Búsqueda por ingredientes
    ingredientes_input = st.text_input("Ingresa los ingredientes separados por comas (ejemplo: tomate, ajo, pollo)")
    if ingredientes_input:
        ingredientes = [ing.strip() for ing in ingredientes_input.split(',')]
        recetas_por_ingredientes = buscar_por_ingredientes(recetas, ingredientes)
        st.write(f"Recetas encontradas con los ingredientes {', '.join(ingredientes)}:")
        for receta in recetas_por_ingredientes:
            st.write(f"**{receta['title']}**")
            st.write(f"**Ingredientes**: {receta['ingredients']}")
            st.write(f"**Tiempo de preparación**: {receta.get('prepTime', 'N/A')} min")
            st.write(f"**Tipo**: {receta.get('type', 'N/A')}")
            st.write(f"**Instrucciones**: {receta['instructions']}")

    # Búsqueda por tiempo de preparación
    tiempo_input = st.number_input("Ingresa el tiempo máximo de preparación en minutos", min_value=1)
    if tiempo_input > 0:
        recetas_por_tiempo = buscar_por_tiempo(recetas, tiempo_input)
        st.write(f"Recetas encontradas con un tiempo de preparación de {tiempo_input} minutos o menos:")
        for receta in recetas_por_tiempo:
            st.write(f"**{receta['title']}**")
            st.write(f"**Ingredientes**: {receta['ingredients']}")
            st.write(f"**Tiempo de preparación**: {receta.get('prepTime', 'N/A')} min")
            st.write(f"**Tipo**: {receta.get('type', 'N/A')}")
            st.write(f"**Instrucciones**: {receta['instructions']}")

    # Búsqueda por tipo de plato
    tipo_input = st.text_input("Ingresa el tipo de plato (ejemplo: entrada, plato principal, postre)")
    if tipo_input:
        recetas_por_tipo = buscar_por_tipo(recetas, tipo_input)
        st.write(f"Recetas encontradas del tipo {tipo_input}:")
        for receta in recetas_por_tipo:
            st.write(f"**{receta['title']}**")
            st.write(f"**Ingredientes**: {receta['ingredients']}")
            st.write(f"**Tiempo de preparación**: {receta.get('prepTime', 'N/A')} min")
            st.write(f"**Tipo**: {receta.get('type', 'N/A')}")
            st.write(f"**Instrucciones**: {receta['instructions']}")
else:
    st.error("No se pudo cargar los datos. Por favor, verifica la URL o el formato de los datos.")
