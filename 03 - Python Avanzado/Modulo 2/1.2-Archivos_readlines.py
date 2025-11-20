
# 1 - Apertura de Archivos
fichero = open("03 - Python Avanzado/Modulo 2/Archivo_write.txt")
# La función (open()), nos permite abrir el fichero

# 2 - Lectura de Lineas
lineas = fichero.readlines() # Creamos la variable (lineas), utilizamos la función (readlines), que nos brinda una lista de todos los elementos, de la variable (fichero) 
print(type(lineas)) # Imprimimos el tipo de dato, de la variable (lineas)
print(lineas) # Imprimimos la variable (lineas)

# 3 - Cierre de Archivos
fichero.close() # La función (close()), nos permite cerrar el fichero
