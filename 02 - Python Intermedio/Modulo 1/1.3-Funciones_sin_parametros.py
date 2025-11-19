
# Función sin Parametros
# Podemos reconocer una función sin parametros cuando no hay ningún valor entre los parentesis
def Suma():
    a = int(input("Ingresar el Número 1: "))
    b = int(input("Ingresar el Número 2: "))
    suma = a + b
    return suma

print(Suma()) # Con el (print) imprimiremos el resultado de la función (Suma)

# Otra forma de plantear una función seria la siguiente:
def Resta():
    a = int(input("Ingrese el Número 1: "))
    b = int(input("Ingrese el Número 2: "))
    resta = a - b
    print(resta) # En este caso el (print) ya se encuentra en la función, por lo tanto podemos llamar directamente a la función (Resta) y ya nos imprimira su resultado

Resta()

# Una forma de usar la función seria la siguiente: Creamos la variables y sus operaciones matematicas, y retornamos las variables
def Calculadora(x, y):
    suma = x + y
    resta = x - y
    multiplicacion = x * y
    division = x / y
    return suma, resta, multiplicacion, division

# Creamos variables para almacenar los resultados y usamos la función creada previamente (Calculadora), dentro del parentesis colocamos los valores a utilizar
a, b, c, d = Calculadora(10, 5)
print(a, b, c, d) # Imprimimos los resultados
