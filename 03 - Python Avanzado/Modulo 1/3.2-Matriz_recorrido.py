
matriz = [] # Creamos la variable (matriz), que se encuentra vacia

ALUMNOS = 4 # Creamos la variable (ALUMNOS), con su respectivo valor
NOTAS = 3 # Creamos la variable (NOTAS), con su respectivo valor

# Llenamos la matriz
for i in range(ALUMNOS): # Utilizamos un (for), con la variable (i) cargamos los datos, que obtendremos con la función (range()) de la variable (ALUMNOS)
    notas = [] # Creamos la variable (notas)
    print("Alumno {}".format(i + 1)) # Imprimimos la cantidad de Alumnos
    for j in range(NOTAS): # Utilizamos un (for), con la variable (j) cargamos los datos, que obtendremos con la función (range()) de la variable (NOTAS)
        nota = float(input("Nota {}: ".format(j + 1))) # Creamos la variable (nota), utilizando un (input) para ingresar las notas, con datos de tipo (float), con la función (.format()) indicamos cual nota estamos cargando 
        notas.append(nota) # Con la función (append()) agregamos los valores de la variable (nota), a la variable (notas)

    matriz.append(notas) # Con la función (append()) agregamos los valores de la variable (nota), a la variable (matriz)

# Recorrer Matriz
print("Recorrido de Matriz por Medio de FOR")

for i in range(ALUMNOS): # Con el primer (for) recorremos todas las filas
    for j in range(NOTAS): # Con el primer (for) recorremos todas las columnas
        # En cada impresión, estaremos imprimiendo los valores que se encuentren en las variables (i, j), con parametro (end=" "), estamos colocando un espacio entre las columnas
        print(matriz[i][j], end=" ") 
    print() # Imprimimos los resultados
