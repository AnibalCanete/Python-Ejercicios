
# Creamos la variable (N) y utilizamos un (input) para ingresar un valor
N = int(input("Ingresar Cantidad de Alumnos: "))

# Con el (for) creamos la variable (i) para recorrer los elementos de la variable (N)
for i in range(N):
    # Creamos la variable (nombre) y utilizamos el (input) para introducir los nombres y imprimirlos junto con la variable (i)
    nombre = input("Nombre {}: ".format(i + 1))
