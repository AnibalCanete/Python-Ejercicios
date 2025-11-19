
# Imprimimos un Titulo
print("Ejemplos con Remove")

# Con la función (remove), podemos eliminar un elemento indicando su valor
# Creamos la lista
lista_letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]
print(lista_letras) # Imprimimos la lista

if "z" in lista_letras: # Verificamos que el elemento se encuentre en la lista 
    lista_letras.remove("z") # Con la función (remove), eliminamos el elemento si se encuentra en la lista
else:
    print("No Esta Dentro de la Lista") # Imprimimos el siguiente mensaje, en caso de que no se encuentre el elemento en la lista

print(lista_letras) # Imprimimos la lista

print("-----Ejemplo 1-----")
# Creamos la lista
lista_letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]
print(lista_letras) # Imprimimos la lista

if "a" in lista_letras:
    lista_letras.remove("a")
else:
    print("No Esta Dentro de la Lista") # Imprimimos el siguiente mensaje, en caso de que no se encuentre el elemento en la lista

print(lista_letras) # Imprimimos la lista con el elemento eliminado
