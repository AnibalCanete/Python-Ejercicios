
# Creamos la variable (pbi), que seria una matriz
pbi = [
    [2.9, 2.5], [3.9, 4.0], [0.9, 2.2], [1.5, 3.3],
    [1.8, 2.6], [1.0, 2.0], [2.2, 2.3], [4.0, 4.0],
    [2.5, 3.5], [3.0, 3.0], [-9.5, -8.5]
]

FILAS = 11 # Creamos la variable (FILAS), con su respectivo valor
COLUMNAS = 2 # Creamos la variable (COLUMNAS), con su respectivo valor

def recorrer_matriz():
    for i in range(FILAS): # Con el primer (for) recorremos todas las filas
        for j in range(COLUMNAS): # Con este segundo (for), recorremos todas las columnas
            # En cada impresión, estaremos imprimiendo los valores que se encuentren en las variables (f, c), con parametro (end=" "), estamos colocando un espacio entre las columnas  
            print(pbi[i][j], end=" ") 
        print() # Imprimimos los resultados

print("Antes") # Imprimimos un mensaje para indicar la matriz previa a modificarla 
recorrer_matriz() # Llamamos a la función (recorrer_matriz())
pbi[2][1] = 999 # Utilizando los indices, indicamos cual fila y columna seran modificadas
print("Despues") # Imprimimos un mensaje para indicar la matriz posterior a modificarla
recorrer_matriz() # Llamamos a la función (recorrer_matriz())

