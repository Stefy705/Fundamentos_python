# INVENTARIO DE LA TIENDA ESCOLAR
 # INDICES     0            1              2             3           4           5              6
productos = ["Esferos", "Marcadores", "Cuadernos", "Papel crepe", "Lapices", "Borradores", "Cartulinas"]
precios = [1500.00, 14500.50, 6800.50, 2300.00, 3200.00, 5500.00, 1400.00]
cantidades = [20, 15, 25, 24, 35, 10, 22]

# Cuantos productos tiene el inventario
cantidad_productos = len(productos)


#Imprimir las 3 listas

print("---------------------Inventario de la tienda escolar: -------------------"
    "\nProductos:", productos,
    "\nPrecios:", precios, 
    "\nCantidades:", cantidades,
    "\nCantidad productos:", cantidad_productos )

print(f"\nEl producto {productos[0]} tiene un precio de {precios[0]} pesos y una cantidad disponible de {cantidades[0]} unidades.\n")
print(f"El producto {productos[1]} tiene un precio de {precios[1]} pesos y una cantidad disponible de {cantidades[1]} unidades.\n")
print(f"El producto {productos[2]} tiene un precio de {precios[2]} pesos y una cantidad disponible de {cantidades[2]} unidades.\n")
print(f"El producto {productos[3]} tiene un precio de {precios[3]} pesos y una cantidad disponible de {cantidades[3]} unidades.\n")
print(f"El producto {productos[4]} tiene un precio de {precios[4]} pesos y una cantidad disponible de {cantidades[4]} unidades.\n")
print(f"El producto {productos[5]} tiene un precio de {precios[5]} pesos y una cantidad disponible de {cantidades[5]} unidades.\n")
print(f"El producto {productos[6]} tiene un precio de {precios[6]} pesos y una cantidad disponible de {cantidades[6]} unidades.\n")

print(type(productos)) # esto es una class list 
print(type(productos[0])) # esto es una class str
