# -*- coding: utf-8 -*-

"""
Este script calcula la temperatura promedio de varias ciudades
a partir de datos semanales.
"""

# 1. DATOS: Temperaturas de 3 ciudades durante 4 semanas.
# Se utiliza un diccionario donde cada ciudad es una clave y su valor es una lista de temperaturas.
datos_temperaturas = {
    "Quito": [15, 17, 16, 14],
    "Guayaquil": [28, 30, 29, 28],
    "Cuenca": [12, 11, 13, 12]
}


def calcular_temperaturas_promedio(datos):
    """
    Calcula la temperatura promedio para cada ciudad en un diccionario de datos.

    Esta función recorre el diccionario de ciudades, calcula el promedio de las
    temperaturas registradas para cada una y devuelve un nuevo diccionario
    con los promedios.

    Args:
        datos (dict): Un diccionario donde las claves son los nombres de las ciudades (str)
                      y los valores son listas de temperaturas (list of int/float).

    Returns:
        dict: Un diccionario con los nombres de las ciudades como claves y sus
              temperaturas promedio como valores.
    """
    # Se crea un diccionario vacío para almacenar los promedios.
    promedios = {}

    # Se itera sobre cada ciudad y su lista de temperaturas en el diccionario de datos.
    # El método .items() nos permite obtener tanto la clave (ciudad) como el valor (temps).
    for ciudad, temps in datos.items():
        # Se calcula el promedio: suma de las temperaturas dividida por la cantidad de registros.
        promedio = sum(temps) / len(temps)

        # Se almacena el resultado en el diccionario de promedios, asociando la ciudad con su promedio.
        promedios[ciudad] = promedio

    return promedios


# --- Pruebas y Verificación ---
# Se llama a la función con nuestros datos para obtener los promedios.
promedios_calculados = calcular_temperaturas_promedio(datos_temperaturas)

# Se imprime el resultado de una manera clara y legible.
print("--- Temperaturas Promedio Calculadas ---")
for ciudad, promedio in promedios_calculados.items():
    # Se formatea el promedio para mostrar solo dos decimales usando f-strings.
    print(f"La temperatura promedio en {ciudad} es: {promedio:.2f}°C")