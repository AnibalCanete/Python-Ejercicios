
# 1 - Apertura de Archivos
fichero = open("03 - Python Avanzado/Modulo 2/Archivo_write.txt")
# La función (open()), nos permite abrir el fichero

oracion = fichero.readline() # Creamos la variable (oracion), y utilizamos la función (readline()) en la variable (fichero)
while oracion != "": # Con el bucle (while) recorremos la variable (oracion) hasta que se cumpla la condición, siempre que la variable (oracion) sea diferente al vacio, ejecutara el bucle
    print(oracion, end="") # Imprimimos la variable (oracion) y como segundo parametro agregamos un vacio (end="")
    oracion = fichero.readline() # Utilizamos la variable (oracion), y utilizamos la función (readline()) en la variable (fichero)

