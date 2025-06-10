import re


def validar_nombre(nombre):
    # Expresión regular: dos palabras, cada una inicia con mayúscula y sigue con minúsculas
    patron = r'^[A-Z][a-z]+ [A-Z][a-z]+$'
    return bool(re.match(patron, nombre))


# Ejemplo de uso
nombre_usuario = "jo Nu"
if validar_nombre(nombre_usuario):
    print("Nombre válido")
else:
    print("Nombre inválido")
