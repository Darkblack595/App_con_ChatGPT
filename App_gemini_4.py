import streamlit as st
import re

# Título de la app
st.title("ID Validator")
st.markdown("<h6>Hecha por Juan Pablo Gaviria Orozco</h6>", unsafe_allow_html=True)

# Función para validar Cédula de Ciudadanía (Colombia)
def validar_cedula_colombia(cedula):
    patron = re.compile(r'^\d{10}$')
    return patron.match(cedula) is not None

# Función para validar CURP (México)
def validar_curp_mexico(curp):
    patron = re.compile(r'^[A-Z]{4}[0-9]{6}[HM][A-Z0-9]{2}$')
    return patron.match(curp) is not None

# Función para validar Número de Seguro Social (SSN) (Estados Unidos)
def validar_ssn_usa(ssn):
    patron = re.compile(r'^\d{3}-\d{2}-\d{4}$')
    return patron.match(ssn) is not None

# Input del usuario
opcion = st.selectbox("Selecciona el tipo de identificación a validar", ["Cédula de Ciudadanía (Colombia)", "CURP (México)", "SSN (Estados Unidos)"])
identificacion = st.text_input("Ingresa la identificación")

# Validar según la opción seleccionada
if st.button("Validar"):
    if opcion == "Cédula de Ciudadanía (Colombia)":
        if validar_cedula_colombia(identificacion):
            st.success("La Cédula de Ciudadanía es válida.")
        else:
            st.error("La Cédula de Ciudadanía no es válida.")
    
    elif opcion == "CURP (México)":
        if validar_curp_mexico(identificacion):
            st.success("El CURP es válido.")
        else:
            st.error("El CURP no es válido.")
    
    elif opcion == "SSN (Estados Unidos)":
        if validar_ssn_usa(identificacion):
            st.success("El SSN es válido.")
        else:
            st.error("El SSN no es válido.")
