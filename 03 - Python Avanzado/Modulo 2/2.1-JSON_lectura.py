
import json # Importamos el paquete (json)

# Leemos el archivo JSON
with open("03 - Python Avanzado/Modulo 2/JSON_Ejemplo_1.json", "r") as json_file:
    data = json.load(json_file) # Con la función (load()) propia del paquete (json) podemos cargar el archivo en la variable (data)
    diccionario = data # Creamos la variable (diccionario) y utilizamos la variable (data) para utilizarlo los datos, en la variable (diccionario)
    # print(data) # Imprimimos la variable (data), nos imprime todos los datos sin una forma especifica

    print(diccionario) # Imprimimos la variable (diccionario)

    # Nos sirve para imprimir las claves del diccionario
    print("Nombre:", diccionario["Nombre"])
    print("Apellido:", diccionario["Apellido"])
    print("Edad", diccionario["Edad"])
    print("Documento", diccionario["Documento"])
    print("Ciudad", diccionario["Ciudad"])
    print("Pais:", diccionario["Pais"])

    # Utilizamos la función (dumps), para imprimir la información de la variable (data) y con (indent=) le indicamos la indentación que tendra la libreria 
    print(json.dumps(data, indent=2)) 
