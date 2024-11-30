def depurar_datos(data):
    series = []
    nombres_producto = []
    valores = []
    fechas = []
    contactos = []

    for index, row in data.iterrows():
        text = ' '.join(row.dropna().astype(str))  # Combinar todas las columnas en una sola cadena de texto

        # Número de serie del producto (números de 6 dígitos)
        serie = re.search(r"\b\d{6}\b", text)
        series.append(serie.group(0) if serie else "N/A")

        # Información de contacto (nombre de la persona, correo y número de teléfono)
        contacto_nombre = re.search(r"([A-Z][a-z]+(?:\s[A-Z][a-z]+)?)", text)
        contacto_email_tel = re.findall(r"(\+\d{1,3}\s?\d+|\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b)", text)
        contacto = [contacto_nombre.group(0) if contacto_nombre else "N/A"]
        contacto.extend(contacto_email_tel)
        contactos.append(', '.join(contacto) if contacto else "N/A")

        # Descartar nombres de personas para la búsqueda del nombre del producto
        text = text.replace(contacto_nombre.group(0) if contacto_nombre else "", "")

        # Nombre del producto (una sola palabra con una letra inicial en mayúscula)
        nombre_producto = re.search(r"\b[A-Z][a-z]*\b", text)
        nombres_producto.append(nombre_producto.group(0) if nombre_producto else "N/A")

        # Valor del producto (comienza con $, uno o dos dígitos después del punto)
        valor = re.search(r"\$([0-9]+\.[0-9]{1,2})", text)
        valores.append(valor.group(0) if valor else "N/A")

        # Fecha de compra del producto (contiene /)
        fecha = re.search(r"\b\d{2}/\d{2}/\d{2}\b", text)
        fechas.append(fecha.group(0) if fecha else "N/A")

    depurado_data = pd.DataFrame({
        "Número de Serie": series,
        "Nombre del Producto": nombres_producto,
        "Valor": valores,
        "Fecha de Compra": fechas,
        "Contacto": contactos
    })

    return depurado_data
