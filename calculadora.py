print("Calculadora de operaciones")

valor_uno = float(input("Ingrese el primer valor: ")) 
valor_dos = float(input("Ingrese el segundo valor: "))

tipoOperacion = input("Elija la operacion que quiere realizar: \
 1.suma  \
 2.resta  \
 3.multiplicacion  \
 4.division: ")

suma = valor_uno + valor_dos
resta = valor_uno - valor_dos
multiplicacion = valor_uno * valor_dos
division = valor_uno / valor_dos




if tipoOperacion == "1":
    print("El resultado de la suma es:", suma)
if tipoOperacion == "2":
    print("El resultado  de la resta es :", resta)

if tipoOperacion == "3":
    print("El resultado de la multiplicacion es:", multiplicacion)
if tipoOperacion == "4":
    print("El resultado de la division es:", division)

