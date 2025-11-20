
# 1 - Apertura de Archivos
fichero = open("03 - Python Avanzado/Modulo 2/Archivo_write.txt")

# La función (open()), nos permite abrir el fichero

# 2 - Lectura de Linea
linea = fichero.readline() # Creamos la variable (linea), donde utilizamos la variable (fichero) y usamos la función (readline), para leer una linea del archivo
print(type(linea)) # Imprimimos que tipo de dato es la variable (linea)
print(linea) # Imprimimos la variable (linea), en este caso seria una sola linea del fichero
print(fichero.readline()) # Imprimimos un linea del fichero, en este caso, seria la segunda linea 

# 3 - Cierre de Archivos
fichero.close() # La función (close()), nos permite cerrar el fichero
