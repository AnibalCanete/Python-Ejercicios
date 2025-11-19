
# Creamos la variable (lista_letras) con sus respectivos valores
lista_letras = ["a", "b", "c", "d", "e"]
variable = "2"

if variable in lista_letras: # Verificamos que el valor ("2") de la variable se encuentre en la lista
    posicion = lista_letras.index(variable) # Solicitamos el indice, con la función (index()) podemos saber en que posición se encuentra el elemento 
    print("Esta en la Posición: ", posicion) # En caso de que el elemento se encuentre en la lista, imprimimos su posición
else:
    print("No hay Elemento en la Lista") # En caso de que no exista dicho elemento en la lista, imprimimos el siguiente mensaje

print("-----Ejemplo 1-----")

lista_nombres = ["Lucas", "Juan", "Pedro", "Rocio", "Ana", "Emilia"]
nombre_existe = "Emilia"

if nombre_existe in lista_nombres:
    posicion = lista_nombres.index(nombre_existe)
    print("Esta en la Posición: ", posicion)
else:
    print("No hay Elemento en la Lista")

print("-----Ejemplo 2-----")

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numero_existe = 5

if numero_existe in lista_numeros:
    posicion = lista_numeros.index(numero_existe)
    print("Esta en la Posición: ", posicion)
else:
    print("No hay Elemento en la Lista")
