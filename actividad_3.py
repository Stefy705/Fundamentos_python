from multiprocessing import Value

#INPUT la entrada de informacion del usuario
print("=" *25)
print("   CLASIFICADOR DE  IMC ")
print("=" *25)
print()


peso_kg = float(input("Ingrese su peso en Kg: "))
estatura_m = float(input("Ingrese su altura en metros: "))
#
imc = peso_kg / (estatura_m ** 2)
if (peso_kg >= 0 and estatura_m >= 0):
    print("\n----🔸Calculando su indice de masa corporal🔸...")
    print(f"\n🗒️ Su indice de masa corporal es: {round(imc, 2)} kg/m² \n")
        
    if imc < 18.5:
            print("Usted tiene bajo peso🫥, necesita alimentarse mejor")
    elif imc >= 18.5 and imc < 24.9:
     print("Usted tiene un peso normal⚖️, siga así🏋🏻")
    elif imc >= 25 and imc < 29.9:
        print(" Usted tiene sobrepeso🐻‍❄️, necesita hacer ejercicio") 
    elif imc >= 30:
     print("Usted tiene Obesidad🐋, necesita buscar ayuda profesional")
else:
    print("Error: Por favor ingrese un valor numerico valido positivo.❌")
