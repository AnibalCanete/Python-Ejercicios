
# 1 - Apertura de Archivos
fichero = open("03 - Python Avanzado/Modulo 2/Archivo_write.txt", "w")
# La función (open()), nos permite abrir el fichero, colocando el (w) como segundo parametro podemos escribir en el archivo, 
# y poniendo un nombre en la ruta acompañado de (.txt) podemos crear un archivo desde cero

lista = ["Manzana\n", "Pero\n", "Plátano\n"] # Creamos la variable (lista), con sus respectivos valores

fichero.writelines(lista) # Con la función (writelines) podemos sobreescribir de manera mas rapida el texto mediante una lista, en este caso utilizamos la variable (lista)
fichero.close() # Cerramos el archivo con la función (close())
