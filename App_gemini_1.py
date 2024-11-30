import streamlit as st
import re

# Título de la app
st.title("Evaluador de Fortaleza de Contraseñas")
st.markdown("<h6>Hecha por Juan Pablo Gaviria Orozco</h6>", unsafe_allow_html=True)

# Entrada de la contraseña
password = st.text_input("Introduce tu contraseña", type="password")

# Función para evaluar la fortaleza de la contraseña
def evaluate_password(password):
    suggestions = []
    if len(password) < 8:
        suggestions.append(("La contraseña debe tener al menos 8 caracteres.", "red"))
    if not re.search("[a-z]", password):
        suggestions.append(("La contraseña debe incluir al menos una letra minúscula.", "orange"))
    if not re.search("[A-Z]", password):
        suggestions.append(("La contraseña debe incluir al menos una letra mayúscula.", "orange"))
    if not re.search("[0-9]", password):
        suggestions.append(("La contraseña debe incluir al menos un número.", "yellow"))
    if not re.search("[^a-zA-Z0-9]", password):
        suggestions.append(("La contraseña debe incluir al menos un carácter especial.", "green"))
    return suggestions

# Botón para evaluar la contraseña
if st.button("Evaluar"):
    suggestions = evaluate_password(password)
    if suggestions:
        st.warning("La contraseña no cumple con los siguientes criterios de seguridad:")
        for suggestion, color in suggestions:
            st.markdown(f"<div style='border:1px solid {color}; padding: 10px; border-radius: 5px; background-color: {color}; color: white;'>{suggestion}</div>", unsafe_allow_html=True)
    else:
        st.success("¡Tu contraseña es segura!")

