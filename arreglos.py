# Definir dimensiones
ciudades = ["Quito", "Guayaquil", "Cuenca"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 2  # Número de semanas

# Crear matriz 3D de temperaturas (ciudades x días x semanas)
# Ejemplo con datos ficticios
import random
matriz = [[[random.randint(10, 30) for _ in range(len(dias))] for _ in range(semanas)] for _ in range(len(ciudades))]

# Calcular promedio por ciudad y semana
for i, ciudad in enumerate(ciudades):  # Recorre ciudades
    print(f"\nPromedios de temperatura en {ciudad}:")
    for j in range(semanas):  # Recorre semanas
        suma = 0
        for k in range(len(dias)):  # Recorre días
            suma += matriz[i][j][k]
        promedio = suma / len(dias)
        print(f"  Semana {j+1}: {promedio:.2f} °C")


    
