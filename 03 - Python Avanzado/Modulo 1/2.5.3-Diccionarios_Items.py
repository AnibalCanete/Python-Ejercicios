
# Creamos el diccionario (d), con sus respectivos valores
d = {
    "A": 1,
    "B": 2
}

it = d.items() # Con la función (items()), nos sirve para traernos el diccionario en forma de lista con sus claves y valores
print(it) # Imprimimos el valor de la variable (it)
print(list[it]) # Convertimos el valor de la variable (it) a una lista

# Obtenemos el valor del primer elemento, ya que es una tupla, el primer elemento seria para señalar el elemento general de la lista y 
# el segundo para indicar que elemento de la tupla que deseamos obtener
print(list(it)[0][0]) 
