
# Se llama While Anidado, porque utiliza un bucle repetitivo dentro de otro bucle repetitivo
# Crear un Programa que Permite Ingresar los Nombres de N alumnos y la cantidad de Cursos
# Declaramos la variable (N) y utilizamos un (input) para ingresar un valor 
N = int(input("Ingresar Cantidad de Estudiantes: "))
i = 1 # Declaramos la variable (i) con el valor (1) para cargar los nombres de los estudiantes

# Con el (while) establecemos la condición que debe cumplirse
while N >= i:
    # Declaramos la variable (nombre) con un (input) para introducir los nombres de los estudiantes
    nombre = input("Alumno {}: ".format(i)) # Con las llaves ({}) y el (.format()) podemos imprimir los nombres de los estudiantes
    # Declaramos la variable (M) y utilizamos un (input) para introducir un valor 
    M = int(input("Ingresar Cantidad de Cursos: "))
    j = 0 # Declaramos la variable (j) con el valor (0) para cargar los nombres de los cursos

    # Con el (while) establecemos la condición que debe cumplirse
    while M > j:
        # Declaramos la variable (curso_nombre) y utilizamos un (input) para introducir los nombres de los cursos
        curso_nombre = input("Curso {}: ".format(j + 1)) # Con las llaves ({}) y el (.format()) imprimimos los nombres y incrementamos el valor de la variable (j)
        j += 1 # Incrementamos la variable (j) de 1 en 1

    i += 1 # Incrementamos la variable (i) de 1 en 1
    