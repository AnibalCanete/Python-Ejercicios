
# 1 - Apertura de Archivos
fichero= open("03 - Python Avanzado/Modulo 2/Archivo_write.txt", "r")

# La función (open()), nos permite abrir el fichero

# "r": Por defecto, para leer el fichero
# "w": Para escribir en el fichero

# 2 - Lectura de todo el fichero 
print(fichero.read()) # La función (read()), nos permite leer el fichero

# 3 - Cierre de archivos
fichero.close() # La función (close), nos permite cerrar el fichero

