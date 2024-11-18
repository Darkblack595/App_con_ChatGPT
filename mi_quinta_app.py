import streamlit as st
import numpy as np

# Título y autor
st.title("Calculadora de Operaciones Matriciales")
st.subheader("Hecho por Juan Pablo Gaviria Orozco")

# Restricciones
st.write("""
**Restricciones:**
- Las matrices pueden tener un tamaño máximo de 10x10.
- Se pueden ingresar hasta 5 matrices para las operaciones que lo requieran.
""")

# Menú principal
menu = st.sidebar.selectbox(
    "Selecciona una operación:",
    [
        "Suma de Matrices",
        "Diferencia de Matrices",
        "Producto Cruz",
        "Producto Punto",
        "Matriz Inversa",
        "Determinante",
    ],
)

# Función para ingresar matrices
def ingresar_matrices(max_matrices, max_dim):
    matrices = []
    num_matrices = st.number_input(
        f"¿Cuántas matrices deseas ingresar? (máximo {max_matrices})",
        min_value=1,
        max_value=max_matrices,
        step=1,
        value=1,
    )
    for i in range(num_matrices):
        st.write(f"**Matriz {i + 1}:**")
        filas = st.number_input(f"Filas de la matriz {i + 1}", min_value=1, max_value=max_dim, step=1, value=2)
        columnas = st.number_input(f"Columnas de la matriz {i + 1}", min_value=1, max_value=max_dim, step=1, value=2)
        matriz = []
        for f in range(filas):
            fila = st.text_input(f"Fila {f + 1} de la matriz {i + 1} (separa los valores con comas):")
            if fila:
                matriz.append([float(x) for x in fila.split(",")])
        if len(matriz) == filas and all(len(row) == columnas for row in matriz):
            matrices.append(np.array(matriz))
        else:
            st.error("Por favor, verifica las dimensiones y los valores ingresados.")
    return matrices

# Función para mostrar resultado
def mostrar_resultado(resultado, nombre_operacion):
    st.subheader(f"Resultado de la operación: {nombre_operacion}")
    if isinstance(resultado, np.ndarray):
        st.write("Resultado:")
        st.write(resultado)
    elif isinstance(resultado, list):
        for i, res in enumerate(resultado):
            st.write(f"Matriz {i + 1}:")
            st.write(res)
    else:
        st.write(resultado)

# Operaciones
if menu == "Suma de Matrices":
    st.header("Suma de Matrices")
    st.write("Puedes sumar hasta 5 matrices del mismo tamaño.")
    matrices = ingresar_matrices(5, 10)
    if len(matrices) > 1:
        try:
            resultado = sum(matrices)
            mostrar_resultado(resultado, "Suma de Matrices")
        except ValueError:
            st.error("Todas las matrices deben tener el mismo tamaño.")

elif menu == "Diferencia de Matrices":
    st.header("Diferencia de Matrices")
    st.write("Puedes restar hasta 5 matrices del mismo tamaño.")
    matrices = ingresar_matrices(5, 10)
    if len(matrices) > 1:
        try:
            resultado = matrices[0]
            for m in matrices[1:]:
                resultado = resultado - m
            mostrar_resultado(resultado, "Diferencia de Matrices")
        except ValueError:
            st.error("Todas las matrices deben tener el mismo tamaño.")

elif menu == "Producto Cruz":
    st.header("Producto Cruz")
    st.write("Solo se permite operar con 2 vectores de tamaño 3x1 o 1x3.")
    matrices = ingresar_matrices(2, 3)
    if len(matrices) == 2 and all(m.shape in [(3,), (3, 1), (1, 3)] for m in matrices):
        try:
            resultado = np.cross(matrices[0].flatten(), matrices[1].flatten())
            mostrar_resultado(resultado, "Producto Cruz")
        except ValueError:
            st.error("Error al calcular el producto cruz. Verifica las dimensiones.")

elif menu == "Producto Punto":
    st.header("Producto Punto")
    st.write("Solo se permite operar con 2 vectores o matrices compatibles para multiplicación.")
    matrices = ingresar_matrices(2, 10)
    if len(matrices) == 2:
        try:
            resultado = np.dot(matrices[0], matrices[1])
            mostrar_resultado(resultado, "Producto Punto")
        except ValueError:
            st.error("Las dimensiones de las matrices no son compatibles para el producto punto.")

elif menu == "Matriz Inversa":
    st.header("Matriz Inversa")
    st.write("Solo se permite operar con una matriz cuadrada.")
    matrices = ingresar_matrices(1, 10)
    if len(matrices) == 1 and matrices[0].shape[0] == matrices[0].shape[1]:
        try:
            resultado = np.linalg.inv(matrices[0])
            mostrar_resultado(resultado, "Matriz Inversa")
        except np.linalg.LinAlgError:
            st.error("La matriz no es invertible.")

elif menu == "Determinante":
    st.header("Determinante")
    st.write("Solo se permite operar con una matriz cuadrada.")
    matrices = ingresar_matrices(1, 10)
    if len(matrices) == 1 and matrices[0].shape[0] == matrices[0].shape[1]:
        try:
            resultado = np.linalg.det(matrices[0])
            mostrar_resultado(resultado, "Determinante")
        except np.linalg.LinAlgError:
            st.error("Error al calcular el determinante. Verifica la matriz.")
