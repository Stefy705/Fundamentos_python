 
print("\n  *ANALISIS DE TEMPERATURAS SEMANALES* \n")

#INDICES:        0   1   2   3   4   5   6   7   8   9   10  11  12  13
#indexnegativo -14  -13 -12 -11 -10 -9  -8  -7  -6  -5  -4  -3  -2  -1
#                1   2   3  4    5   6   7   8   9  10   11  12  13  14
temperaturas = [18, 21, 19, 24, 22, 20, 17, 23, 25, 21, 18, 20, 22, 19]

print(f"El primer dia tuvo una temperatura de {temperaturas[-14]}°C \n"
      f"El ultimo dia tuvo una temperatura de {temperaturas[13]}°C \n"
      f"El septimo dia tuvo una temperatura de {temperaturas[6]}°C \n"
      f"El penultimo dia tuvo una temperatura de {temperaturas[-2]}°C")

# Usa slicing para extraer e imprimir
print(f"En la primera semana hubo temperaturas de {temperaturas[-14:-7]}°C \n"
# La segunda semana solo los dias pares 
      f"En la segunda semana hubo temperaturas de {temperaturas[7:]}°C")

#La temperatura en invertido
temperaturas.reverse()
print(f"Las temperaturas al reves {temperaturas}°C")

# EL PROMEDIO
promedio1 = sum(temperaturas[0:7]) / len(temperaturas[0:7])
print(f"El promedio de la primera semana es:{round(promedio1)}grados ")
promedio2 = sum(temperaturas[7:14]) / len(temperaturas[7:14])
print(f"El promedio de la segunda semana es:{round(promedio2)}grados ")







