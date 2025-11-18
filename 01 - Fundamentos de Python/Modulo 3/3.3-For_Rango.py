
# For con Range, utilizamos un rango para recorrer los elementos de una variable
# Con el (range) hacemos que la variable (element) que utilizamos recorra hasta un número antes del valor que tenemos
for element in range(10):
    print(element) # Imprimimos la variable

# Cuando utilizamos dos parametros en el (range) el primer parametro seria el inicio (5) y el segundo el final (10)
for item in range(5, 10):
    print(item) # Imprimimos la variable

# Cuando utilizamos tres parametros en el (range) el primero es el inicio (1), el segundo es hasta antes de (100), y el tercero indica de cuanto en cuanto se aumenta (10)
for element in range(1, 100, 10):
    print(element) # Imprimimos la variable
    