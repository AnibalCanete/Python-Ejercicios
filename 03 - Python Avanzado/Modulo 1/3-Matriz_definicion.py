
# Una matriz es una lista de listas

matriz = [] # Creamos una matriz vacia

FILAS = 4 # Creamos la variable (FILA), con su respectivo valor
COLUMNAS = 6 # Creamos la variable (COLUMNAs), con su respectivo valor

# Llenamos la Matriz
# Con el (for) utilizamos la variable (i) para usarlo como indice, con la función (range()), utilizamos la variable (FILAS) para recorrer el número de veces que posee dicha variable
for i in range(FILAS): 
    fila = [0] * COLUMNAS # Creamos la variable (fila), la cual multiplicamos con la variable (COLUMNAS)
    matriz.append(fila) # Utilizamos la función (append()) para agregar los elementos a la variable (matriz)

print(matriz) # Imprimamos la variable (matriz)
