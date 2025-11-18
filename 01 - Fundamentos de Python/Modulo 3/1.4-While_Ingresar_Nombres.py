
# Crear un Programa que permite ingresar los nombres de N alumnos
# Declaramos la variable (N), con un (input) para ingresar un valor
N = int(input("Ingresar Cantidad de Estudiantes: "))

# Declaramos la variable (i), para poder hacer le bucle finito
i = 1

# Con el (while) establecemos la condición que debe cumplirse
while N >= i:
    # Declaramos la variable (nombre) y utilizamos un (input) para introducir un valor, con las llaves ({}) y el (.format()) hacemo que el valor de (i) se imprima
    nombre = input("Nombre {}: ".format(i))
    i += 1 # Incrementamos la variable de 1 en 1 (Tambien podemos escribir esta linea de la siguiente manera: i = 1 + 1)
    