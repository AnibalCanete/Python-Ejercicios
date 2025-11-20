
# Importamos el paquete (json)
import json 

# Un objeto de tipo diccionario
obj = {
    "Nombre": "Juan",
    "Apellido": "Perez",
    "Edad": 25,
    "Documento": 10203040,
    "Ciudad": "Lima",
    "Pais": "Peru"
}

# Guardar en un Archivo JSON
with open("03 - Python Avanzado/Modulo 2/JSON_Ejemplo_1.json", "w") as outfile: # Con el (as) convertimos en variable la dirección a utilizar, colocandole un nombre
    # Convertir a JSON
    # La función (dump), sirve para escribir un archivo jshon dentro de la carpeta, el primer parametro es lo que se introducira, 
    # y la segunda es la variable que representa el archivo
    json.dump(obj, outfile) 
