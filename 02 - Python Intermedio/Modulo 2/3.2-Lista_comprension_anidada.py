
# Matriz: Lista de Lista
C = [
    [2, 3, 4],
    [40, 50, 60],
    [100, 200, 300]
]

# Equivalente usando For
total = 0
for row in C: # La variable (row), con el (for) va a recorrer toda la lista (C)
    for x in row: # La variable (x), con el (for) va recorrer toda la variable (row)
        total += x # Creamos la variable (total), donde se sumaran todos los elementos
print(total) # Imprimimos la variable (total)

# Suma Total
# Con la variable (x) recorremos la variable (row) de la lista (C), con el (for) recorremos la variable (x) de la lista (row)
total_comprension = [x for row in C for x in row] 
print(total_comprension) # Imprimimos la variable (total_comprension)
print(sum(total_comprension)) # Imprimimos la suma de todos los elementos de la lista 
