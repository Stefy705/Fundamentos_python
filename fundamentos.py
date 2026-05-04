from tkinter import E


print ("Hello world")
#TIPOS DE ESCRITURA EN PYTHON

camelCase = "holaMundo"
PascalCase = "HolaMundo"
snake_case = "hola_mundo"
#TIPOS DE VARIABLES
X= "esta x en mayuscula"
x= "esta x en minuscula"
print(X)
print(x)

#TIPOS DE DATOS



# CASTEO ES CAMBIAR EL TIPO DE DATO DE UNA VARIABLE A OTRO DIFERENTE


"""
comentario
por 
bloques

"""

# INDENTACION EN PYTHON
if 5 > 2 :
    print("5 es mayor que 2")
else:
    print("5 no es mayor que 2")   


# INPUT EN PYTHON
nombre_usuario = input("Ingrese su nombre: ")
print("Bienvenido", nombre_usuario)
# todo dato con input se toma como string, por lo que cambiamos ese tipo de dato con casteo
years = int(input("Ingrese su edad: "))
print("Tu edad es:", years)
# para unir texto con variables se puede usar f-string
print(f"Hola, tu nombre es {nombre_usuario} y tu edad es {years} años")
