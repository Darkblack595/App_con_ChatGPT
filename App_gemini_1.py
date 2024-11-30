import streamlit as st
import re

def evaluar_contrasena(contrasena):
    """Evalúa la fortaleza de una contraseña y proporciona sugerencias amigables."""

    # Expresiones regulares para verificar los criterios de seguridad
    mayusculas = re.search(r'[A-Z]', contrasena)
    minusculas = re.search(r'[a-z]', contrasena)
    numeros = re.search(r'\d', contrasena)
    especiales = re.search(r'[^a-zA-Z0-9]', contrasena)

    # Verificar la longitud mínima
    longitud = len(contrasena) >= 8

    # Evaluar la fortaleza y generar sugerencias amigables
    if all([mayusculas, minusculas, numeros, especiales, longitud]):
        return "¡Felicidades! Tu contraseña es muy fuerte y segura."
    else:
        sugerencias = []
        if not longitud:
            sugerencias.append("¡Añade más letras y números! Las contraseñas fuertes son como rompecabezas largos.\n")
        if not mayusculas:
            sugerencias.append("Incluye una letra mayúscula. ¡Las mayúsculas le dan un toque extra de seguridad!\n")
        if not minusculas:
            sugerencias.append("¡Agrega una letra minúscula! Varía las letras para hacerla más difícil de adivinar.\n")
        if not numeros:
            sugerencias.append("¡Incorpora un número! Los números hacen que tu contraseña sea más resistente a ataques.\n")
        if not especiales:
            sugerencias.append("¡Utiliza un símbolo especial! Los símbolos como !, @, #, $, %, ^, & y * añaden una capa extra de protección.\n")
        return "Tu contraseña podría ser más fuerte. Aquí tienes algunas ideas para mejorarla: " + ", ".join(sugerencias)

# Título de la aplicación
st.title("Evaluador de Contraseñas")
st.markdown("**Hecho por Juan Pablo Gaviria Orozco**")

# Estilos CSS
st.markdown("""
<style>
.stApp {
  font-family: 'sans-serif';
}
.stTitle {
  font-size: 36px;
  text-align: center;
  color: #336699;
}
.stButton > button {
  background-color: #4CAF50;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer; 1 
}
.sugerencia {
  padding: 15px;
  border-radius: 5px;
  margin-bottom: 10px;
}
.sugerencia-1 {
  background-color: #f2f2f2;
}
.sugerencia-2 {
  background-color: #e0e0e0;
}
.sugerencia-3 {
  background-color: #d4d4d4;
}
.sugerencia-4 {
  background-color: #b3b3b3;
}
</style>
""", unsafe_allow_html=True)

# ... (resto de tu código)

# Si la contraseña no es fuerte, mostrar sugerencias en recuadros de colores
if "fuerte" not in resultado:
    st.markdown("<div class='sugerencias'>**Aquí hay algunas sugerencias para fortalecer tu contraseña:**</div>", unsafe_allow_html=True)
    for i, sugerencia in enumerate(resultado.split(", "), start=1):
        st.markdown(f"<div class='sugerencia sugerencia-{i}'>{sugerencia}</div>", unsafe_allow_html=True)
