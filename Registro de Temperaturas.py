# Crear una matriz 3D que represente los datos de temperaturas diarias en varias ciudades.
# En una dimensión, puedes tener diferentes ciudades, en otra dimensión, días de la semana
# (Lunes, Martes, Miércoles, etc.), y en la tercera dimensión, semanas.
# Dentro de cada celda de la matriz, puedes almacenar las temperaturas diarias para una ciudad
# en un día específico de una semana determinada.
# Utilizar bucles anidados para calcular el promedio de temperaturas para una ciudad por cada
# una de las semanas.
# Mostrar el promedio de temperaturas para cada ciudad y semana en la pantalla.
ciudades = ["Puyo", "Quito", "Guayaquil"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 3

# Crear la matriz 3D [ciudad][semana][día]
# Simularemos temperaturas aleatorias para simplificar
import random
matriz_temperaturas = [
    [  # para cada ciudad
        [random.randint(10, 30) for _ in dias]  # temperaturas
        for _ in range(semanas)  # semanas
    ]
    for _ in ciudades
]
# Calcular promedios con bucles anidados
for i, ciudad in enumerate(ciudades):  # recorrer ciudades
    print(f"\nCiudad: {ciudad}")
    for s in range(semanas):  # recorrer semanas
        suma = 0
        for d in range(len(dias)):  # recorrer días
            suma += matriz_temperaturas[i][s][d]
        promedio = suma / len(dias)
        print(f"  Semana {s+1}: Promedio de temperatura = {promedio:.2f}°C")

