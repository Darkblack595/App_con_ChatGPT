import streamlit as st

# Título
st.title("Mi primera app")

# Autor
st.write("Esta app fue elaborada por “Juan Pablo Gaviria Orozco”.")

# Entrada de usuario
nombre_usuario = st.text_input("Por favor, escribe tu nombre:")

# Saludo personalizado
if nombre_usuario:
    st.write(f"{nombre_usuario}, te doy la bienvenida a mi primera app.")
