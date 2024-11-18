import streamlit as st

# Título
st.title("Conversor Universal")

# Marca
st.write("Hecho por Juan Pablo Gaviria Orozco")

# Descripción
st.write("Selecciona una categoría y el tipo de conversión que deseas realizar.")

# Categorías de conversión
categorias = [
    "Temperatura",
    "Longitud",
    "Peso/Masa",
    "Volumen",
    "Tiempo",
    "Velocidad",
    "Área",
    "Energía",
    "Presión",
    "Tamaño de datos"
]

categoria_seleccionada = st.selectbox("Selecciona una categoría:", categorias)

# Lógica de conversiones
if categoria_seleccionada == "Temperatura":
    conversiones = [
        "Celsius a Fahrenheit",
        "Fahrenheit a Celsius",
        "Celsius a Kelvin",
        "Kelvin a Celsius"
    ]
    seleccion = st.selectbox("Selecciona el tipo de conversión:", conversiones)
    valor = st.number_input("Ingresa el valor a convertir:")

    if seleccion == "Celsius a Fahrenheit":
        resultado = (valor * 9/5) + 32
    elif seleccion == "Fahrenheit a Celsius":
        resultado = (valor - 32) * 5/9
    elif seleccion == "Celsius a Kelvin":
        resultado = valor + 273.15
    elif seleccion == "Kelvin a Celsius":
        resultado = valor - 273.15

elif categoria_seleccionada == "Longitud":
    conversiones = [
        "Pies a metros",
        "Metros a pies",
        "Pulgadas a centímetros",
        "Centímetros a pulgadas"
    ]
    seleccion = st.selectbox("Selecciona el tipo de conversión:", conversiones)
    valor = st.number_input("Ingresa el valor a convertir:")

    if seleccion == "Pies a metros":
        resultado = valor * 0.3048
    elif seleccion == "Metros a pies":
        resultado = valor / 0.3048
    elif seleccion == "Pulgadas a centímetros":
        resultado = valor * 2.54
    elif seleccion == "Centímetros a pulgadas":
        resultado = valor / 2.54

elif categoria_seleccionada == "Peso/Masa":
    conversiones = [
        "Libras a kilogramos",
        "Kilogramos a libras",
        "Onzas a gramos",
        "Gramos a onzas"
    ]
    seleccion = st.selectbox("Selecciona el tipo de conversión:", conversiones)
    valor = st.number_input("Ingresa el valor a convertir:")

    if seleccion == "Libras a kilogramos":
        resultado = valor * 0.453592
    elif seleccion == "Kilogramos a libras":
        resultado = valor / 0.453592
    elif seleccion == "Onzas a gramos":
        resultado = valor * 28.3495
    elif seleccion == "Gramos a onzas":
        resultado = valor / 28.3495

elif categoria_seleccionada == "Volumen":
    conversiones = [
        "Galones a litros",
        "Litros a galones",
        "Pulgadas cúbicas a centímetros cúbicos",
        "Centímetros cúbicos a pulgadas cúbicas"
    ]
    seleccion = st.selectbox("Selecciona el tipo de conversión:", conversiones)
    valor = st.number_input("Ingresa el valor a convertir:")

    if seleccion == "Galones a litros":
        resultado = valor * 3.78541
    elif seleccion == "Litros a galones":
        resultado = valor / 3.78541
    elif seleccion == "Pulgadas cúbicas a centímetros cúbicos":
        resultado = valor * 16.3871
    elif seleccion == "Centímetros cúbicos a pulgadas cúbicas":
        resultado = valor / 16.3871

elif categoria_seleccionada == "Tiempo":
    conversiones = [
        "Horas a minutos",
        "Minutos a segundos",
        "Días a horas",
        "Semanas a días"
    ]
    seleccion = st.selectbox("Selecciona el tipo de conversión:", conversiones)
    valor = st.number_input("Ingresa el valor a convertir:")

    if seleccion == "Horas a minutos":
        resultado = valor * 60
    elif seleccion == "Minutos a segundos":
        resultado = valor * 60
    elif seleccion == "Días a horas":
        resultado = valor * 24
    elif seleccion == "Semanas a días":
        resultado = valor * 7

elif categoria_seleccionada == "Velocidad":
    conversiones = [
        "Millas por hora a kilómetros por hora",
        "Kilómetros por hora a metros por segundo",
        "Nudos a millas por hora",
        "Metros por segundo a pies por segundo"
    ]
    seleccion = st.selectbox("Selecciona el tipo de conversión:", conversiones)
    valor = st.number_input("Ingresa el valor a convertir:")

    if seleccion == "Millas por hora a kilómetros por hora":
        resultado = valor * 1.60934
    elif seleccion == "Kilómetros por hora a metros por segundo":
        resultado = valor / 3.6
    elif seleccion == "Nudos a millas por hora":
        resultado = valor * 1.15078
    elif seleccion == "Metros por segundo a pies por segundo":
        resultado = valor * 3.28084

elif categoria_seleccionada == "Área":
    conversiones = [
        "Metros cuadrados a pies cuadrados",
        "Pies cuadrados a metros cuadrados",
        "Kilómetros cuadrados a millas cuadradas",
        "Millas cuadradas a kilómetros cuadrados"
    ]
    seleccion = st.selectbox("Selecciona el tipo de conversión:", conversiones)
    valor = st.number_input("Ingresa el valor a convertir:")

    if seleccion == "Metros cuadrados a pies cuadrados":
        resultado = valor * 10.7639
    elif seleccion == "Pies cuadrados a metros cuadrados":
        resultado = valor / 10.7639
    elif seleccion == "Kilómetros cuadrados a millas cuadradas":
        resultado = valor * 0.386102
    elif seleccion == "Millas cuadradas a kilómetros cuadrados":
        resultado = valor / 0.386102

elif categoria_seleccionada == "Energía":
    conversiones = [
        "Julios a calorías",
        "Calorías a kilojulios",
        "Kilovatios-hora a megajulios",
        "Megajulios a kilovatios-hora"
    ]
    seleccion = st.selectbox("Selecciona el tipo de conversión:", conversiones)
    valor = st.number_input("Ingresa el valor a convertir:")

    if seleccion == "Julios a calorías":
        resultado = valor / 4.184
    elif seleccion == "Calorías a kilojulios":
        resultado = valor * 0.004184
    elif seleccion == "Kilovatios-hora a megajulios":
        resultado = valor * 3.6
    elif seleccion == "Megajulios a kilovatios-hora":
        resultado = valor / 3.6

elif categoria_seleccionada == "Presión":
    conversiones = [
        "Pascales a atmósferas",
        "Atmósferas a pascales",
        "Barras a libras por pulgada cuadrada",
        "Libras por pulgada cuadrada a bares"
    ]
    seleccion = st.selectbox("Selecciona el tipo de conversión:", conversiones)
    valor = st.number_input("Ingresa el valor a convertir:")

    if seleccion == "Pascales a atmósferas":
        resultado = valor / 101325
    elif seleccion == "Atmósferas a pascales":
        resultado = valor * 101325
    elif seleccion == "Barras a libras por pulgada cuadrada":
        resultado = valor * 14.5038
    elif seleccion == "Libras por pulgada cuadrada a bares":
        resultado = valor / 14.5038

elif categoria_seleccionada == "Tamaño de datos":
    conversiones = [
        "Megabytes a gigabytes",
        "Gigabytes a Terabytes",
        "Kilobytes a megabytes",
        "Terabytes a petabytes"
    ]
    seleccion = st.selectbox("Selecciona el tipo de conversión:", conversiones)
    valor = st.number_input("Ingresa el valor a convertir:")

    if seleccion == "Megabytes a gigabytes":
        resultado = valor / 1024
    elif seleccion == "Gigabytes a Terabytes":
        resultado = valor / 1024
    elif seleccion == "Kilobytes a megabytes":
        resultado = valor / 1024
    elif seleccion == "Terabytes a petabytes":
        resultado = valor / 1024

# Mostrar resultado
if "resultado" in locals():
    st.write(f"Resultado: {resultado}")
