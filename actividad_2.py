print("================================")
print("CALCULADORA DE PROMEDIO DE NOTAS")
print("================================\n")

#CALCULO DEL PROMEDIO - solicitar al usuario que ingrese las notas, se castea en float
nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))
promedio = (nota1 + nota2 + nota3)/3 

print("\n-----------------PROMEDIO---------------- \n")
print(f"El promedio de las notas es: {round(max(0, promedio), 2)} puntos")

#CALCULO PARA ALCANZAR LA NOTA MAXIMA
nota_maxima = 5.0
nota_faltante = nota_maxima - promedio 
print("\n ¿CUANTO FALTO PARA ALCANZAR LA NOTA MAXIMA? \n")
print(f"Faltaron {round(nota_faltante, 2)} puntos ")

print("\n--------------RESULTADO DE APROBACIÓN------------ \n")
# calculo si el estudiantee aprueba o no 
if (promedio >= 3.0):
    print("El estudiante aprobó el examen ✅ 🥳\n")
else:
    print("El estudiante no aprobó el examen ❌😒\n")

print("🎉Gracias por usar la calculadora de notas🎉\n")
    


