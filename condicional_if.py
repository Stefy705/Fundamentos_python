#CONDICIONAL IF / ELIF / ELSE

from encodings.punycode import T


# if False:
#     print("La condicion es verdadera")
# elif False: 
#     print("La segunda condicion es verdadera en elif")
# elif True:
#     print("esta condicion es verdadera en elif")
# else:
#     print("La condicion es falsa")


# Ejercicio: clasificacion de Edad
# edad = 19
# if edad < 18:
#     print("Eres menor de edad")
# elif edad >= 18 and edad < 65:
#     print("Eres un joven adulto")
# else:
#     print("Eres un adulto mayor")

# Ejercicio de clasificscion de edad con if anidados
edad = int(input("Ingrese su edad oara ser clasificada: "))
if edad < 18:
    if edad >= 12 and edad < 18:
        print("eres un adolecente")
    else:
        print("eres un niño")
else: 
    if edad >= 18 and edad <= 60:
        print("eres un adulto ")


# OPERADOR TERNARIO
numero = int(input("Ingrese un numero: "))
if numero % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")
    print("El numero es par if numero % 2 == 0 else 'El numero es impar' ")

