
# Un diccionario anidado, es un diccionario que contiene otro diccionario
dic1 = {"Nombre": "Jorge", "Edad": 25, "Nota": 19.5} # Creamos un diccionario (dic1)
dic2 = {"Nombre": "Omar", "Edad": 26, "Nota": 12} # Creamos un diccionario (dic2)

# Creamos un diccionario (d)
d = {
    1: dic1, # Tenemos como clave (1), un numero entero y su valor (dic1), es un diccionario 
    2: dic2 # Tenemos como clave (2), un numero entero y su valor (dic2), es un diccionario
}

print(d) # Imprimimos el diccionario (d)
