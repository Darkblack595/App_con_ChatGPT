import streamlit as st
import re

# Título de la app
st.title("Validador de Datos")
st.markdown("<h6>Hecho por Juan Pablo Gaviria Orozco</h6>", unsafe_allow_html=True)

# Funciones de validación con expresiones regulares
def validar_nombre(nombre):
    if re.fullmatch(r"[A-Z][a-zA-Z]*", nombre):
        return True
    else:
        return False

def validar_correo(correo):
    if re.fullmatch(r"[^@]+@[^@]+\.[a-zA-Z]{2,}", correo):
        return True
    else:
        return False

def validar_telefono(telefono):
    if re.fullmatch(r"\d{10,}", telefono):
        return True
    else:
        return False

def validar_fecha(fecha):
    if re.fullmatch(r"\d{2}/\d{2}/\d{2}", fecha):
        return True
    else:
        return False

# Campos de entrada
nombre = st.text_input("Nombre", placeholder="Ej: Juan", help="Solo letras y la primera con mayúscula")
correo = st.text_input("Correo Electrónico", placeholder="Ej: ejemplo@dominio.com")
telefono = st.text_input("Número de Teléfono", placeholder="Ej: 1234567890")
fecha = st.text_input("Fecha de Nacimiento", placeholder="dd/mm/AA", help="Formato: dd/mm/AA")

# Botón para validar
if st.button("Validar"):
    es_valido = True
    if not validar_nombre(nombre):
        st.error("Nombre inválido. Debe comenzar con mayúscula y contener solo letras.")
        es_valido = False
    if not validar_correo(correo):
        st.error("Correo electrónico inválido. Debe seguir el formato nombre@dominio.com.")
        es_valido = False
    if not validar_telefono(telefono):
        st.error("Número de teléfono inválido. Debe contener al menos 10 dígitos.")
        es_valido = False
    if not validar_fecha(fecha):
        st.error("Fecha inválida. Debe seguir el formato dd/mm/AA.")
        es_valido = False

    if es_valido:
        st.success("¡Todos los datos son válidos!")

