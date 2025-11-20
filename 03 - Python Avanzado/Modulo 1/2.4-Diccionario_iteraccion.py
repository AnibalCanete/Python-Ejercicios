
# Creamos el diccionario
d1 = {
    "Nombre": "Juan",
    "Edad": 24,
    "Documento": 10203040
}

# 1 - Imprimir las llaves (key) del diccionario
for x in d1: # Utilizamos el (for) podemos recorrer el diccionario (d1) con la variable (x) almacenamos sus datos
    print(x) # Imprimimos las claves del diccionario almacenadas en la variable (x)

# 2 - Imprime los valores del diccionario
for x in d1: # Utilizando el (for) podemos recorrer el diccionario (d1) con la variable (x) almacenamos sus datos
    # Imprimimos los valores de las claves del diccionario, utilizamos el nombre del diccionario (d1) y entre corchetes ([]), 
    # colocamos la variable (x) que tiene almacenados los datos del diccionario 
    print(d1[x]) 

# 3 - Imprime las llaves (key) y los valores (value) del diccionario
for x, y in d1.items(): # Con el (for), utilizamos variables (x, y) y recorremos el diccionario (d1), y con la función (items()), recogemos sus datos
    print(x, y) # Imprimimos las variables (x, y)

