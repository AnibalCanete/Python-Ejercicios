
# Imprimimos un Titulo
print("Ejemplo con POP")

# Si se necesita eliminar un elemento por su posición en la lista, se puede utilizar la función (pop())
# Por defecto, (pop()) eliminará el último de la lista y retornará el valor del elemento eliminado.

# Creamos la lista (lista_letras)
lista_letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]
print(lista_letras) # Imprimimos la lista

# Creamos la variable (x) y utilizamos la función (pop()) para eliminar el último elemento
x = lista_letras.pop()
print(x) # Imprimimos el elemento eliminado

x = lista_letras.pop() # Eliminamos otro elemento mas
print(x) # Imprimimos el elemento eliminado
print(lista_letras) # Imprimimos la lista ya con los elementos eliminados
