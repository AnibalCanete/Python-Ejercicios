
import requests # Recordar instalar el paquete en Python
import json

# Parametro
name = input("Ingrese Nombre: ") # Ingresamos el nombre que queremos consultar

# URL del API REST
url = "https://api.nationalize.io/?name=" + name # Concatenamos la URL con la variable (name)

# Invocamos el servicio Web
# Se recibe en un diccionario 
result = requests.get(url).json() # Con la variable (result), utilizamos la función (get()) del paquete (requests), para obtener la url, luego lo convertimos al formato JSON

# Muestra el Resultado
print(json.dumps(result, indent=4)) # Imprimimos el resultado, con un formato  mas entendible JK
