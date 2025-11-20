
# 1 - Apertura de Archivos
fichero = open("03 - Python Avanzado/Modulo 2/Archivo_write.txt", "w")
# La función (open()), nos permite abrir el fichero, colocando el (w) como segundo parametro podemos escribir en el archivo, 
# y poniendo un nombre en la ruta acompañado (.txt) podemos crear un archivo desde cero

# 2 - Escritura al Texto
fichero.write("Contenido a Escribir\n") # Con la función (write) escribimos en el fichero
fichero.write("Segunda linea de contenido\n") # El (\n) nos permite colocar un salto de linea
fichero.write("Tercera linea de contenido\n") # Escribimos una tercera linea

# 3 - Cierre de Archivos
fichero.close() # La función (close()), nos permite cerrar el fichero
