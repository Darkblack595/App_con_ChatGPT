import streamlit as st
import re
from datetime import datetime

# Título de la app
st.title("Validador de Datos")
st.markdown("<h6>Hecho por Juan Pablo Gaviria Orozco</h6>", unsafe_allow_html=True)

# Funciones de validación con expresiones regulares
def validar_nombre(nombre):
    if re.fullmatch(r"[A-Z][a-zA-Z]*( [A-Z][a-zA-Z]*)*", nombre):
        return True
    else:
        return False

def validar_correo(correo):
    if re.fullmatch(r"[^@]+@[^@]+\.[a-zA-Z]{2,}", correo):
        return True
    else:
        return False

def validar_telefono(telefono):
    if re.fullmatch(r"\d{7,10}", telefono):
        return True
    else:
        return False

def validar_fecha(fecha):
    try:
        datetime.strptime(fecha, "%d/%m/%y")
        return True
    except ValueError:
        return False

def es_bisiesto(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def validar_fecha_detallada(fecha):
    try:
        day, month, year = map(int, fecha.split('/'))
        if month < 1 or month > 12:
            return False
        if day < 1 or day > 31:
            return False
        if month == 2:
            if es_bisiesto(year) and day > 29:
                return False
            elif not es_bisiesto(year) and day > 28:
                return False
        if month in [4, 6, 9, 11] and day > 30:
            return False
        return True
    except:
        return False

# Campos de entrada
nombre = st.text_input("Nombre", placeholder="Ej: Juan Pablo", help="Solo letras, primera en mayúscula")
correo = st.text_input("Correo Electrónico", placeholder="Ej: ejemplo@dominio.com")

paises = {
    "Colombia": "+57",
    "Estados Unidos": "+1",
    "México": "+52",
    "España": "+34",
    "Argentina": "+54"
}

pais = st.selectbox("Seleccione su país", list(paises.keys()))
telefono = st.text_input(f"Número de Teléfono ({paises[pais]})", placeholder="Ej: 1234567890")

fecha = st.text_input("Fecha de Nacimiento", placeholder="dd/mm/AA", help="Formato: dd/mm/AA")

# Botón para validar
if st.button("Validar"):
    es_valido = True
    if not validar_nombre(nombre):
        st.markdown("<div style='border:1px solid red; padding: 10px; border-radius: 5px; background-color: red; color: white;'>Nombre inválido. Debe comenzar con mayúscula y contener solo letras y espacios en blanco.</div>", unsafe_allow_html=True)
        es_valido = False
    if not validar_correo(correo):
        st.markdown("<div style='border:1px solid orange; padding: 10px; border-radius: 5px; background-color: orange; color: white;'>Correo electrónico inválido. Debe seguir el formato nombre@dominio.com.</div>", unsafe_allow_html=True)
        es_valido = False
    if not validar_telefono(telefono):
        st.markdown(f"<div style='border:1px solid yellow; padding: 10px; border-radius: 5px; background-color: yellow; color: black;'>Número de teléfono inválido para {pais}. Verifique la longitud y el formato.</div>", unsafe_allow_html=True)
        es_valido = False
    if not validar_fecha_detallada(fecha):
        st.markdown("<div style='border:1px solid green; padding: 10px; border-radius: 5px; background-color: green; color: white;'>Fecha inválida. Verifique el formato y la validez del día, mes y año bisiesto.</div>", unsafe_allow_html=True)
        es_valido = False

    if es_valido:
        st.success("¡Todos los datos son válidos!")

