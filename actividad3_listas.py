# # Lista de canciones
# cancionesFavoritas = ["Nuestro año","Solo","Labios de papel","Despidete bien","Mas tuyo"]
# print(f"Canciones favoritas: {cancionesFavoritas}")

# # Cancion nueva agregada al final
# cancionesFavoritas.append("Lo que me hacia bien")
# print(f"La cancion del final cambio {cancionesFavoritas}")

# # Cancion nueva agregada de segundas
# cancionesFavoritas.insert(2, "Control")
# print(f"La segunda cancion se cambio {cancionesFavoritas}")

# # Estamos combinando 2 listas
# bonusTrack = ["BonusTrack 1", "Bonus Track 2"]
# cancionesFavoritas.extend(bonusTrack)
# print(f"La lista se combino con bonusTrack {cancionesFavoritas}")

# # Remover una cancion
# cancionesFavoritas.remove("Control")
# print(f"Se removio una cancion {cancionesFavoritas}")

# # Eliminar la ultima cancion
# cancionesFavoritas.pop()
# print(f"Se elimino la ultima cancion {cancionesFavoritas}")

# # Lista ordenada
# cancionesFavoritas.sort()
# print(f"Lista ordenada alfabeticamente {cancionesFavoritas}")

# # preguntas
# """
# ¿Cuantas canciones tiene la playlist?
# """
# print(len(cancionesFavoritas))
  
# """
# ¿En qué posición está la primera canción que agregaste?
# """
# posicion = cancionesFavoritas.index("Lo que me hacia bien")
# print(f"La posicion de la primera cancion que agregue fue {posicion}")

# """
# ¿Cuántas veces aparece el string 'Bonus Track 1'?
# """

# veces = cancionesFavoritas.count("BonusTrack 1")
# print(f"Aparece las siguientes veces {veces}")

#  --------------MI LISTA DE CANCIONES STEFY-----------------
cancionesFav = ["Still loving you", "Paranoid", "Come as you are", "Die for you", "Wicked game"]
print(f"Mis canciones favoritas son: {cancionesFav}")
# agregar una cancion nueva al final
cancionesFav.append("Birds of a feather")
print(f"La cancion agregada del final:{cancionesFav}")
#Cancion agregada de segundas
cancionesFav.insert(2, "Para que regreses")
print(f"La segunda cancion se cambio a: {cancionesFav}")
# Para combinar 2 listas
bonusTrack = ["BonusTrack1", "BonusTrack2"]
cancionesFav.extend(bonusTrack)
# Para remover una cancion
cancionesFav.remove("Still loving you")
print(f"Se removio la cancion still loving you: {cancionesFav}")
#Se elimina la ultima cancion
cancionesFav.pop()
print(f"Se elimino la ultima cancion {cancionesFav}")
#Lista ordenada
cancionesFav.sort()
print(f"Lista ordenada alfabeticamente {cancionesFav}")
# preguntas

#¿Cuantas canciones tiene la playlist?
print(len(cancionesFav))
#¿En qué posición está la primera canción que agregaste?

posicion = cancionesFav.index("Paranoid")
print(f"La posicion de la primera cancion que agregue fue {posicion}")

#¿Cuántas veces aparece el string 'Bonus Track 1'?
veces = cancionesFav.count("BonusTrack 1")
print(f"Aparece las siguientes veces {veces}")