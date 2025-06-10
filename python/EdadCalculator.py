from datetime import date


def es_mayor_de_edad(fecha_nacimiento: date, edad_minima: int = 18) -> bool:
    hoy = date.today()
    # Calcula la edad real (teniendo en cuenta día y mes)
    edad = hoy.year - fecha_nacimiento.year - (
        (hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day)
    )
    return edad >= edad_minima


# Ejemplo de uso:
# Suponiendo que la persona nació el 15 de julio de 2000
fecha_nac = date(2010, 7, 15)
if es_mayor_de_edad(fecha_nac):
    print("Es mayor de 18 años")
else:
    print(r'"Es menor de 18 años"')
