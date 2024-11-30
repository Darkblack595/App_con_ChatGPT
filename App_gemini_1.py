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
            sugerencias.append("¡Añade más letras y números! Las contraseñas fuertes son como rompecabezas largos.")
        if not mayusculas:
            sugerencias.append("Incluye una letra mayúscula. ¡Las mayúsculas le dan un toque extra de seguridad!")
        if not minusculas:
            sugerencias.append("¡Agrega una letra minúscula! Varía las letras para hacerla más difícil de adivinar.")
        if not numeros:
            sugerencias.append("¡Incorpora un número! Los números hacen que tu contraseña sea más resistente a ataques.")
        if not especiales:
            sugerencias.append("¡Utiliza un símbolo especial! Los símbolos como !, @, #, $, %, ^, & y * añaden una capa extra de protección.")
        return "Tu contraseña podría ser más fuerte. Aquí tienes algunas ideas para mejorarla: " + ", ".join(sugerencias)

# Título de la aplicación
st.title("Evaluador de Contraseñas ")
st.markdown("**Hecho por Juan Pablo Gaviria Orozco**")

# Explicación de los criterios
st.write("""
Una contraseña fuerte es como una caja fuerte: ¡cuanto más compleja, más difícil de abrir! 
Para que tu contraseña sea realmente segura, te recomendamos que cumpla los siguientes criterios:

* **Al menos 8 caracteres:** Cuanto más larga, mejor.
* **Mayúsculas y minúsculas:** Combina letras grandes y pequeñas para hacerla más variada.
* **Números:** Los números añaden una capa extra de seguridad.
* **Caracteres especiales:** Símbolos como !, @, #, $, %, ^, & y * hacen tu contraseña más difícil de adivinar.
""")

# Campo de entrada para la contraseña
contrasena = st.text_input("Ingrese su contraseña:")

# Botón para evaluar la contraseña
if st.button("Evaluar mi contraseña"):
    resultado = evaluar_contrasena(contrasena)
    st.success(resultado)
