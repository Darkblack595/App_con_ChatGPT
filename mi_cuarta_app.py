import streamlit as st

# Título y autor
st.title("Gestión del PAPA")
st.subheader("Hecho por Juan Pablo Gaviria Orozco")

# Menú principal
menu = st.sidebar.selectbox("Selecciona una opción:", ["PAPA Global", "PAPA por Tipología"])

# Función para calcular el PAPA
def calcular_papa(creditos_notas):
    total_peso = sum(credito * nota for credito, nota in creditos_notas)
    total_creditos = sum(credito for credito, _ in creditos_notas)
    return total_peso / total_creditos if total_creditos > 0 else 0

# Ventana de "PAPA Global"
if menu == "PAPA Global":
    st.header("Cálculo del PAPA Global")
    
    # Variables de sesión para almacenar los datos
    if "papa_global" not in st.session_state:
        st.session_state["papa_global"] = []

    # Entrada de datos
    with st.form("form_global"):
        creditos = st.number_input("Número de Créditos (materia)", min_value=1, step=1, value=1, key="creditos_global")
        nota = st.number_input("Nota obtenida (materia)", min_value=0.0, step=0.01, value=0.0, key="nota_global")
        agregar = st.form_submit_button("Agregar Materia")
    
    # Agregar datos a la lista
    if agregar:
        st.session_state["papa_global"].append((creditos, nota))
        st.success("Materia agregada correctamente.")

    # Mostrar materias y cálculo del PAPA
    if st.session_state["papa_global"]:
        st.subheader("Materias registradas")
        for i, (credito, nota) in enumerate(st.session_state["papa_global"]):
            st.write(f"Materia {i + 1}: Créditos = {credito}, Nota = {nota}")
        
        papa = calcular_papa(st.session_state["papa_global"])
        st.write(f"**PAPA Global = {papa:.2f}**")

    # Botón para limpiar los cálculos
    if st.button("Limpiar cálculo global"):
        st.session_state["papa_global"] = []
        st.success("Cálculos globales limpiados.")

# Ventana de "PAPA por Tipología"
elif menu == "PAPA por Tipología":
    st.header("Cálculo del PAPA por Tipología")
    
    # Variables de sesión para almacenar datos por tipología
    if "papa_tipologia" not in st.session_state:
        st.session_state["papa_tipologia"] = {tipo: [] for tipo in ["Básica", "Profesional", "Electiva"]}

    # Selección de tipología
    tipologia = st.selectbox("Selecciona la tipología:", ["Básica", "Profesional", "Electiva"])
    
    # Entrada de datos
    with st.form("form_tipologia"):
        creditos = st.number_input(
            f"Número de Créditos ({tipologia})", min_value=1, step=1, value=1, key=f"creditos_{tipologia}"
        )
        nota = st.number_input(
            f"Nota obtenida ({tipologia})", min_value=0.0, step=0.01, value=0.0, key=f"nota_{tipologia}"
        )
        agregar = st.form_submit_button(f"Agregar Materia a {tipologia}")
    
    # Agregar datos a la lista correspondiente
    if agregar:
        st.session_state["papa_tipologia"][tipologia].append((creditos, nota))
        st.success(f"Materia agregada correctamente a la tipología {tipologia}.")

    # Mostrar materias y cálculo del PAPA por tipología
    if st.session_state["papa_tipologia"][tipologia]:
        st.subheader(f"Materias registradas ({tipologia})")
        for i, (credito, nota) in enumerate(st.session_state["papa_tipologia"][tipologia]):
            st.write(f"Materia {i + 1}: Créditos = {credito}, Nota = {nota}")
        
        papa_tipologia = calcular_papa(st.session_state["papa_tipologia"][tipologia])
        st.write(f"**PAPA para {tipologia} = {papa_tipologia:.2f}**")

    # Botón para limpiar los cálculos por tipología
    if st.button(f"Limpiar cálculo de {tipologia}"):
        st.session_state["papa_tipologia"][tipologia] = []
        st.success(f"Cálculos para {tipologia} limpiados.")
