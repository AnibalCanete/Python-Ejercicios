
# Imprimimos un Titulo
print("Ejemplos con DEL")

# La función (del), nos permite eliminar un elemento por su posición
# Creamos la lista
lista_letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]
print(lista_letras) # Imprimimos la lista

del lista_letras[3] # Utilizamos la función (del), seguido del nombre de la lista, colocamos entre corchetes ([]) la posición del elemento que vamos a eliminar
print(lista_letras) # Imprimimos la lista ya con el elemento eliminado

del lista_letras[:4] # En los corchetes ([]) colocamos que va a eliminar desde la posición (0) hasta antes de la posición (4)
print(lista_letras) # Imprimimos la lista ya con el recorte eliminado

del lista_letras # Eliminamos la lista completa
