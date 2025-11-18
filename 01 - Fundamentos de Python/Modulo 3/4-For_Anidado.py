
# Crear un Programa que permita ingresar los nombres de (N) alumnos y la cantidad de (M) de cursos por alumno
# Creamos la variable (N) y utilizamos un (input) para ingresar un valor
N = int(input("Ingresar Cantidad de Alumnos: "))

# Con el (for), creamos la variable (i) para recorrer el rango de la variable (N)
for i in range(N):
    # Creamos la variable (nombre) y utilizamos un (input) para ingresar un valor, con el (.format()) imprimimos el valor de (i)
    nombre = input("Alumno {}: ".format(i))
    # Creamos la variable (M) y utilizamos un (input) para ingresar un valor
    M = int(input("Ingresar Cantidad de Cursos: "))
    # Con el (for), creamos la variable (j) para recorrer el rango de la variable (M)
    for j in range(M):
        # Creamos la variable (curso_nombre) y utilizamos un (input) para introducir el nombre del curso y el (.format(j + 1)) nos permite almacenar y imprimir el valor de la variable (j)
        curso_nombre = input("Curso {}: ".format(j + 1))
        