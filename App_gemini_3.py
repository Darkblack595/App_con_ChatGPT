import re
import pandas as pd
import requests
import io
import xlsxwriter

# Función para extraer el nombre de producto
def extraer_nombre_producto(texto):
    patron = r"^[A-Z][a-z]+$"
    match = re.search(patron, texto)
    return match.group(0) if match else "N/A"

# Función para extraer el nombre de persona
def extraer_nombre_persona(texto):
    patron = r"^(?:[A-Z][a-z]+(?:[-']?[A-Z][a-z]+)*\s?)+"
    match = re.search(patron, texto)
    return match.group(0) if match else "N/A"

# Función para extraer el valor
def extraer_valor(texto):
    patron = r"\$([0-9]+\.[0-9]{1,2})"
    match = re.search(patron, texto)
    return match.group(1) if match else "N/A"  # Extrae solo el valor numérico

# Función para extraer la fecha
def extraer_fecha(texto):
    patron = r"\b\d{2}/\d{2}/\d{2}\b"
    match = re.search(patron, texto)
    return match.group(0) if match else "N/A"

# Función para depurar y clasificar datos
def depurar_datos(data):
    series = []
    nombres_producto = []
    valores = []
    fechas = []
    contactos = []

    for index, row in data.iterrows():
        text = ' '.join(row.dropna().astype(str))

        # Número de serie
        serie = re.search(r"\b\d{6}\b", text)
        series.append(serie.group(0) if serie else "N/A")

        # Nombre de persona
        contacto_nombre = extraer_nombre_persona(text)
        contactos.append(contacto_nombre)

        # Descartar nombre de persona para buscar el producto
        if contacto_nombre:
            text = text.replace(contacto_nombre, "")

        # Nombre de producto
        nombre_producto = extraer_nombre_producto(text)
        nombres_producto.append(nombre_producto)

        # Valor
        valor = extraer_valor(text)
        valores.append(valor)

        # Fecha
        fecha = extraer_fecha(text)
        fechas.append(fecha)

    depurado_data = pd.DataFrame({
        "Número de Serie": series,
        "Nombre del Producto": nombres_producto,
        "Valor": valores,
        "Fecha de Compra": fechas,
        "Contacto": contactos
    })

    return depurado_data

# Resto del código (carga de datos, conversión a Excel, etc.)
# ...
