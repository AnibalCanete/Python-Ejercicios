
# 1 - Apertura de archivos
fichero = open("03 - Python Avanzado/Modulo 2/Archivo_write.txt")
# La función (open()), nos permite abrir el fichero

# 2 - Lectura de Linea
lineas = fichero.readlines() # Creamos la variable (lineas) y utilizamos la función (readlines) a la variable (fichero)
for oracion in lineas: # Con el (for), utilizamos la variable (oracion) para recorrer la variable (lineas) 
    print(oracion, end="") # Imprimimos la variable (oracion), y un segundo parametro para agregar los vacios

# 3 - Cierre de Archivos
fichero.close() # La función (close()), nos permite cerrar el fichero 
