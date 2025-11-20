
# Creamos la variable (pbi), que seria un matriz
pbi = [
    [2.9, 2.5], [3.9, 4.0], [0.9, 2.2], [1.5, 3.3],
    [1.8, 2.6], [1.0, 2.0], [2.2, 2.3], [4.0, 4.0],
    [2.5, 3.5], [3.0, 3.0], [-9.5, -8.5]
]

FILAS = 11 # Creamos la variable (FILAS), con su respectivo valor
COLUMNAS = 2 # Creamos la variable (COLUMNAS), con su respectivo valor

for f in range(FILAS): # Con el primer (for) recorremos todas las filas
    for c in range(COLUMNAS): # Con este segundo (for) recorremos todas las columnas
        print(pbi[f][c], end=" ") # En cada impresión, estaremos imprimiendo los valores que se encuentren en las variables (f, c), con parametro (end=" "), estamos colocando un espacio entre las columnas
    print() # Imprimimos los resultados

item = pbi[2][1] # Creamos la variable (item), con la cual buscamos en la matriz (pbi) mediante indices la fila y columna solicitada
print(item) # Imprimimos la variable (item), la cual nos dara el valor almacenado en dicha variable
