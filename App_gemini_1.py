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

# Configuración de la página
st.beta_set_page_config(
    page_title="Evaluador de Contraseñas",
    page_icon="",
    layout="wide"
)

# Título de la aplicación
st.title("Evaluador de Contraseñas ")
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
.sugerencias {
  background-color: #f2f2f2;
  padding: 15px;
  border-radius: 5px;
}
</style>
""", unsafe_allow_html=True)

# Explicación de los criterios
st.markdown("""
Hecho por Juan Pablo Gaviria Orozco
""")

# Campo de entrada para la contraseña
contrasena = st.text_input("Ingrese su contraseña:")

# Botón para evaluar la contraseña
if st.button("Evaluar mi contraseña"):
    resultado = evaluar_contrasena(contrasena)
    st.success(resultado)

    if "fuerte" not in resultado:  # Si la contraseña no es fuerte, mostrar sugerencias
        st.markdown("<div class='sugerencias'>**Aquí hay algunas sugerencias para fortalecer tu contraseña:**</div>", unsafe_allow_html=True)
        for sugerencia in resultado.split(", "):
            st.markdown(f"- {sugerencia}")  

# Este código te proporciona una aplicación completa para evaluar la fuerza de contraseñas con una interfaz atractiva y personalizable. 
# Puedes modificar los colores, fuentes y estilos CSS para adaptarlo a tus preferencias.
