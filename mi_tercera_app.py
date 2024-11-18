import streamlit as st
import pandas as pd
import datetime

# Configuración inicial
st.title("Gestor de Finanzas Personales(Hecho por Juan Pablo Gaviria Orozco)")
st.sidebar.title("Menú")
menu = st.sidebar.selectbox("Selecciona una opción:", ["Registro", "Reportes", "Metas de Ahorro"])

# Inicializar datos
if "finanzas" not in st.session_state:
    st.session_state["finanzas"] = pd.DataFrame(columns=["Fecha", "Tipo", "Categoría", "Monto", "Descripción"])

if "metas" not in st.session_state:
    st.session_state["metas"] = pd.DataFrame(columns=["Meta", "Cantidad", "Fecha Límite", "Progreso"])

# Función para actualizar datos
def agregar_registro(tipo, categoria, monto, descripcion):
    nuevo_registro = pd.DataFrame({
        "Fecha": [datetime.date.today()],
        "Tipo": [tipo],
        "Categoría": [categoria],
        "Monto": [monto],
        "Descripción": [descripcion]
    })
    st.session_state["finanzas"] = pd.concat([st.session_state["finanzas"], nuevo_registro], ignore_index=True)

def agregar_meta(meta, cantidad, fecha_limite):
    nueva_meta = pd.DataFrame({
        "Meta": [meta],
        "Cantidad": [cantidad],
        "Fecha Límite": [fecha_limite],
        "Progreso": [0]
    })
    st.session_state["metas"] = pd.concat([st.session_state["metas"], nueva_meta], ignore_index=True)

# Sección de registro
if menu == "Registro":
    st.header("Registro de Finanzas")
    tipo = st.selectbox("Tipo", ["Ingreso", "Gasto"])
    categoria = st.text_input("Categoría (Ej. Comida, Alquiler, Sueldo)")
    monto = st.number_input("Monto", min_value=0.0, step=0.01)
    descripcion = st.text_area("Descripción")
    
    if st.button("Agregar"):
        agregar_registro(tipo, categoria, monto, descripcion)
        st.success("Registro agregado correctamente.")

    st.subheader("Historial")
    st.dataframe(st.session_state["finanzas"])

# Sección de reportes
elif menu == "Reportes":
    st.header("Reportes Semanales y Mensuales")
    hoy = datetime.date.today()

    # Convertir la columna "Fecha" a datetime si no lo está
    if not st.session_state["finanzas"].empty:
        st.session_state["finanzas"]["Fecha"] = pd.to_datetime(st.session_state["finanzas"]["Fecha"], errors="coerce")

    # Filtros
    intervalo = st.radio("Selecciona el intervalo:", ["Semanal", "Mensual"])
    fecha_inicio = hoy - datetime.timedelta(days=7) if intervalo == "Semanal" else hoy.replace(day=1)
    
    # Filtrar registros dentro del intervalo
    registros_intervalo = st.session_state["finanzas"][
        (st.session_state["finanzas"]["Fecha"] >= pd.to_datetime(fecha_inicio)) &
        (st.session_state["finanzas"]["Fecha"] <= pd.to_datetime(hoy))
    ]

    if not registros_intervalo.empty:
        st.subheader(f"Reporte {intervalo.lower()} del {fecha_inicio} al {hoy}")
        gastos = registros_intervalo[registros_intervalo["Tipo"] == "Gasto"]
        ingresos = registros_intervalo[registros_intervalo["Tipo"] == "Ingreso"]
        
        total_gastos = gastos["Monto"].sum()
        total_ingresos = ingresos["Monto"].sum()
        
        st.write(f"**Total Ingresos:** ${total_ingresos:.2f}")
        st.write(f"**Total Gastos:** ${total_gastos:.2f}")
        st.write(f"**Balance:** ${total_ingresos - total_gastos:.2f}")

        st.subheader("Detalle de Gastos")
        st.dataframe(gastos)
    else:
        st.info(f"No hay registros para el intervalo {intervalo.lower()}.")

# Sección de metas de ahorro
elif menu == "Metas de Ahorro":
    st.header("Metas de Ahorro")
    
    # Formulario para agregar metas
    meta = st.text_input("Nombre de la meta")
    cantidad = st.number_input("Cantidad a ahorrar", min_value=0.0, step=0.01)
    fecha_limite = st.date_input("Fecha límite")
    
    if st.button("Agregar Meta"):
        agregar_meta(meta, cantidad, fecha_limite)
        st.success("Meta agregada correctamente.")
    
    # Mostrar metas existentes
    if not st.session_state["metas"].empty:
        st.subheader("Progreso de Metas")
        metas = st.session_state["metas"]
        
        for i, row in metas.iterrows():
            progreso_actual = st.session_state["finanzas"][
                (st.session_state["finanzas"]["Tipo"] == "Ingreso") &
                (st.session_state["finanzas"]["Descripción"].str.contains(row["Meta"], case=False, na=False))
            ]["Monto"].sum()
            
            metas.loc[i, "Progreso"] = progreso_actual
            
            st.write(f"**{row['Meta']}** - Meta: ${row['Cantidad']:.2f}")
            st.progress(min(progreso_actual / row["Cantidad"], 1))
            st.write(f"Progreso: ${progreso_actual:.2f} / ${row['Cantidad']:.2f}")
    else:
        st.info("No tienes metas registradas.")
