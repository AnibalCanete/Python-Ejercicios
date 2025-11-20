
# 1 - Apertura de Archivos
fichero = open("03 - Python Avanzado/Modulo 2/Archivo_write.txt", "w")
# La función (open()), nos permite abrir el fichero, colocando el (w) como segundo parametro podemos escribir en el archivo, 
# y poniendo un nombre en la ruta acompañado de (.txt) podemos crear un archivo desde cero

# 2 - Tenemos unos datos que queremos guardar
lista = ["Manzana", "Pera", "Plátano"] # Creamos la variable (lista), con sus respectivos valores

# 3 - Guardamos la lista en el fichero
for linea in lista: # Utilizamos el (for), con la variable (linea) para recorrer la variable (lista) 
    # Utilizamos la función (write), con la variable (linea) concatenada con (\n), para utilizar un salto de linea, para escribir en la variable (fichero)
    fichero.write(linea + "\n") 

# 4 - Cierre de Archivos
fichero.close() # La función (close()), nos permite cerrar el fichero
