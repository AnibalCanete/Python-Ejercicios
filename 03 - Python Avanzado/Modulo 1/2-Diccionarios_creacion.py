
# Modo 1
diccionario = dict() # Creamos el diccionario, como los parentesis () estan vacios, es un diccionario vacio
print(diccionario) # Imprimimos el diccionario

# Modo 2
d1 = {
    "Nombre": "Jorge", # Los elementos estan conformados por claves y valores
    "Edad": 25, # En este caso, la clave seria (Edad) y el valor (25)
    "Documento": 10203040 # En este caso, la clave seria (Documento) y el valor (10203040)
}

print(d1) # Imprimimos la variable (d1) que seria el diccionario

# Modo 3
d2 = dict([
    ("Nombre", "Pedro"), # Utilizaremos tuplas para cargar elementos del diccionario, las tuplas estarian separadas por comas (,)
    ("Edad", 25), # En este caso, la tupla tendria como elementos clave (Edad) y el valor (25) de dicha clave, ambos separados por una coma (,)
    ("Documento", 10203040), # En este caso, la tupla tendria como elemento clave (Documento) y el valor (10203040) de dicha clave
])

print(d2) # Imprimimos la variable (d2) que seria el diccionario

# Modo 4
d3 = dict(
    Nombre="Diego", # En este caso, los elementos del diccionario estarian escritos con el nombre de la clave (Nombre) seguido de un es igual (=) con el valor (Pedro) de la clave
    Edad=25, # En este caso, la clave (Edad), tiene como igual (=), el valor (25)
    Documento=10203040 # En este caso, la clave (Documento), tiene como igual (=), el valor (10203040)
)

print(d3) # Imprimimos la variable (d3) que seria el diccionario
