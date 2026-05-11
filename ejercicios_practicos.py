# #------------------------------------------------------
print("Ejercicio 1\n")
name = input("Ingrese su nombre: ")
valorProducto =float(input("Ingrese el valor del producto: "))
promedio = float(input("Ingrese el promedio de sus notas: "))

print(f"Su nombre es: {name}, el valor del producto es: ${valorProducto}, y su promedio es: {promedio}")
# #------------------------------------------------------
print("\n Ejercicio 2\n")

num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))
numf= float(input("Ingrese un número decimal: "))
variable1 = input("Ingrese un texto: ")
variable2 = input("Ingrese otro texto: ")

suma = num1 + num2 + numf
numero_mayor = max(num1, num2, numf)

division_enteros = num1 / num2
division_float = division_enteros / numf

print(f"La suma de los números es: {suma}")
print(f"El número mayor es: {numero_mayor}")
print(f"La división de los números enteros es: {division_enteros}")
print(f"La división con decimales es: {division_float}")
print(f"los textos ingresados son: '{variable1}' y '{variable2}'")
# #------------------------------------------------------
print("\n Ejercicio 3\n")

base = int(input("Ingrese el primer numero: "))
exponente = int(input("Ingrese el exponente:"))

resultado = base ** exponente

print(f"El resultado de la operacion es: {resultado}" )
#----------------------------------------------------------------
print("\nEjercicio 4\n")

import math

print("Halla la raiz solo de los siguientes numeros (2, 8, 9, 27, 28, 55, 121)")

numero = int(input("Ingrese el valor a calcular: "))
raiz = math.sqrt(numero)
print(f"La raiz del numero {numero} es: {raiz}")

#---------------------------------
print("\n Ejercicio 5\n")

nombre_est = input("Nombre del estudiante: ")
vari1 = float(input("Ingrese la nota 1: "))
vari2 = float(input("Ingrese la nota 2: "))
vari3 = float(input("Ingrese la nota 3: "))
vari4 = float(input("Ingrese la nota 4: "))
vari5 = float(input("Ingrese la nota 5: "))

promedio = (vari1 + vari2 + vari3 + vari4 + vari5)/5

print(f"El estudiante {nombre_est} tiene un promedio de: {promedio}")

#---------------------------------------------------------
from re import A
print("\nEjercicio 6\n")

numeroUno = 8
numeroDos = 2
print(f"Los numeros en orden son: {numeroUno} y {numeroDos}")
#Variable auxiliar
numero_Uno = numeroDos
numero_Dos = numeroUno

print(f"Los numeros invertidos son: {numero_Uno} y {numero_Dos}")
#--------------------------------------------
print("\nEjercicio 7")

estado = (5==2) or (2>1)
print(estado)

#----------------------------------------------
print("\nEjercicio 8\n")
resultado = 2 * ((10/2)+ 45*(20*6)-15*(14+38)+(9*2))/8
print(resultado)

#-------------------------------------------------
print("\nEjercicio 9\n")

#Variable del cuadrado
ladoCuadrado = 8
#Calcular area y perimetro del cuadrado
areaCuadrado = ladoCuadrado ** 2
perimetroCuadrado = ladoCuadrado + ladoCuadrado + ladoCuadrado + ladoCuadrado
#Resultado
print(f"El area del cuadrado es: {areaCuadrado} cm")
print(f"El perimetro del cuadrado es: {perimetroCuadrado} cm")

#Variables del triangulo
baseTriangulo = 9
alturaTriangulo = 8 
ladoUnoTriangulo = 8
ladoDosTriangulo = 8
#Calcular area y perimetro del triangulo
areaTriangulo = (baseTriangulo * alturaTriangulo)/2
periTriangulo = ladoUnoTriangulo + ladoDosTriangulo + alturaTriangulo
#Resultados 
print(f"El area del triangulo es: {areaTriangulo} cm")
print(f"El perimetro del triangulo es: {periTriangulo} cm")
#Variable rectangulo 
baseRectangulo = 8
alturaRectangulo = 6

areaRectangulo = baseRectangulo * alturaRectangulo
periRectangulo = 2*(baseRectangulo + alturaRectangulo)
print(f"El area del rectangulo es: {areaRectangulo} cm")
print(f"El perimetro del rectangulo es: {periRectangulo} cm")
#------------------------------------------------------------------
print("\nEjercicio 10\n")

rangoEdad = int(input("Ingrese su edad para categorizar a la que pertenece: "))
if rangoEdad < 0:
    print("Error edad invalida")
elif rangoEdad >= 0 and rangoEdad <=5:
    print("Eres un infante")

elif rangoEdad >= 6 and rangoEdad <=10:
    print("Eres un niño")
elif rangoEdad >=11 and rangoEdad <=15:
    print("Eres un pre adolecente")
elif rangoEdad >=16 and rangoEdad <=18:
    print("Eres un adolecente")
elif rangoEdad >=19 and rangoEdad <=25:
    print("Eres un pre adulto")      
elif rangoEdad >=26 and rangoEdad <=40:
    print("Eres un adulto")
elif rangoEdad >=41 and rangoEdad <=55:
    print("Eres un pre anciano")
else:
    print("Eres un anciano")


