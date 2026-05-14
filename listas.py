#Listas
lista_mixta = ["Hello", 1234, 3.14, True, [1,2,3]]
# estructura de una lista 

# indice:         0         1        2          3         4  
#indice_negativo  -4       -3       -2         -1         0
aprendices = ["camilo", "simon", "santiago", "leonardo", "Stefy"]
print(aprendices)

# # acceder a un elemento de la lista 
print(aprendices [1]) 

# modificar un elemento de lista 
aprendices[2] = "Andres"
print(aprendices) # cambio a santiago por andres

# consultar renagos de elementos de la lista 
print(aprendices[0:2]) # [camilo, simon]
print(aprendices[:2]) # [camilo, simon]
print (aprendices[2:5]) #[santiago, andres, stefy]
print (aprendices[2:]) #[santiago, andres, stefy]
print (aprendices[2:2]) #[] no aparece nada por que lo excluye 
# CONCATENAR LISTAS +
# aprendices_adso = aprendices1 + aprendices2
#print(aprendices_adso)

# UNIR LiSTAS CON EXTEND 
# aprendices1.extend(aprendices2)
 # print(aprendices1)

#MEDIR EL LARGO DE LAS LISTAS CON LEN()
# longitud_adso = len(aprendices_adso)
# print(f"la lista dee aprendices de adso tiene {longitud_adso} elementos.")

 #Contar elementos con Count, es para contar cuantas veces hay un elemento repetido
 # count_felipe = aprendices_adso.count("felipe")
 # print(f"El nombre felipe aparece{count_felipe} veces")

 #SABER EL NUMERO DE INDICE DE UN ELEMENTO
 #  indice_felipe = aprendices_adso.index("felipe")
 # print(f"el nombre felipe se encuentra en el indice {indice_felipe}")
 

 #COPIAR UNA LISTA CON copy()
 # nueva_lista_adso = aprendices_adso.copy()
 # print(nueva_lista_adso)

 # AGREGAR ELEMENTOS (append e insert)
 # nueva_lista_adso.append("falcao")
# print(nueva_lista_adso)

#INSERTAR UN elemento en el indice que yo quiera de la lista insert()
# nueva_lista_adso.insert(1,"james")
# se corre a el numero de indice que se escribio

#ELIMINAR ELEMENTOS CON (remove y pop)
# pop = permite borrar un elemento con el numero indice especifico
# remove = es el metodo que remueve la primera ocurrencia con un  valor especifico, es por valor.

# # nueva_lista_adso.pop(4)
# print(nueva_lista_adso)
# #nueva_lista_adso.remove("alejandro")
# print(nueva_lista_adso)

#COMPROBAR PERTENENCIA con (in)
# if "falcao" in nueva_list_adso:
#    print("Falcao esta en la lista de aprendices de adso")
# else:
#   print("Falcao no esta en la lista de aprendices de adso")

#ORDENAR DE LA A-Z on sort() de manera ascendente
# nueva_lista_adso.sort()
# print(nueva_lista_adso)

# ORDENAR DE LA Z-A con reverse() de manera descendente 
# nueva_lista_adso.reverse()
# print(nueva_lista_adso)

# ELIMINAR TODOS LOS ELEMENTOS DE LA LISTA USO CLEAR 
# nueva_lista_adso.clear()
# print(nueva_lista_adso)