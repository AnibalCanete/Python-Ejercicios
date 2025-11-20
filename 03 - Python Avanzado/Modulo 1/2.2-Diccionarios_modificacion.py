
# Creamos el diccionario
d1 = {
    "Nombre": "Juan", 
    "Edad": 24,
    "Documento": 10203040
}

print(d1) # Imprimimos el diccionario antes de modificarlo
print("Nombre Antes de Modificar: {}".format(d1["Nombre"]))
d1["Nombre"] = "Luis Alberto" # Para modificar un elemento del diccionario, indicamos el nombre del diccionario (d1) y entre corchetes ([]) indicamos que clave vamos a modificar, seguido escribimos el nuevo valor
d1["Edad"] = 25 # En este caso, modificaremos la clave (["Edad"]) con su nuevo valor (25)
d1["Documento"] = 40302010 # En este caso, modificaremos la clave (["Documento"]) con su nuevo valor (40302010)
print("Nombre Despúes de Modificar: {}".format(d1["Nombre"]))
print(d1) # Imprimimos el diccionario despúes de modificarlo
