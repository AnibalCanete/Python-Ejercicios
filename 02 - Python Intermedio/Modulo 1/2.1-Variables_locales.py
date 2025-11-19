
# Creamos la función (numero_mayor)
# Una variable local solamente existe dentro de la función
def numero_mayor(numero_1, numero_2):
    respuesta = False
    # Establecemos la condición de si (numero_1) es mayor que (numero_2)
    if numero_1 > numero_2:
        respuesta = True

    return respuesta # Nos retorna el valor de la variable (respuesta)

# Cuerpo Principal 
x = int(input("Número 1: ")) # Declaramos la variable (x) y introducimos un valor con el (input)
y = int(input("Número 2: ")) # Declaramos la variable (y) y introducimos un valor con el (input)

# Establecemos la condición que debe cumplirse, utilizando la función (numero_mayor), con los valores introducidos
if numero_mayor(x, y):
    print("El Número {} es mayor a {}".format(x, y)) # En caso de que la variable (x) sea mayor que la variable (y), se imprime el resultado
else: # Establecemos la condición que puede cumplirse en caso de que no se cumpla la condición principal
    print("El Número {} es mayor a {}".format(y, x)) # En caso de que la variable (y) sea mayor que la variable (x), se imprima el resultado  
