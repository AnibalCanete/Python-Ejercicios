
# Creamos la lista (numeros)
numeros = [1, 2, 3, 4, 5, 6, 7, 8]
r1 = [] # Creamos una lista vacia, para almacenar los nuevos valores

for item in numeros: # Con el (for) utilizamos la variable (item) para almacenar los valores que hay en la lista (numeros) 
    valor = item * 2 # Creamos la variable (valor), donde multiplicamos los elementos de la variable (item) por 2
    r1.append(valor) # Agregamos a la lista (r1), el resultado de la variable (valor)

print("Listas Utilizando For Normal")
print(r1) # Imprimimos la lista (r1)

# Comprensión de Lista
print("Listas por Comprensión")
# Creamos la variable (r2), entre los corchetes ([]) establecemos la expresión, creamos la variable (e), que multiplicaremos por 2, con el (for) utilizaremos la variable (e) y recorremos la lista (numeros)
r2 = [e * 2 for e in numeros]
print(r2) # Imprimimos la lista (r2)

print("Listas por Comprensión con Condicionales")
r3 = [e * 2 for e in numeros if e > 4] # Le agregamos la condición que los elementos sean del elemento 4 para arriba
print(r3) # Imprimimos la lista
