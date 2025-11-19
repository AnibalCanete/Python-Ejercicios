
# Los parentesis () sirven para ingresar parametros
# Función para sumar
def suma(a, b):
    suma = a + b
    return suma # Sirve para retornar el valor de la variable (suma)

print(suma(5, 3)) # Imprimimos el resultado de la suma usando la función (suma)

# Otra forma de imprimir el resultado seria la siguiente:
sumatoria = suma(5, 7)
print(sumatoria)

# Función para Restar 
def resta(a, b):
    resta = a - b
    return resta

# Una forma de imprimir el resultado de la resta
print(resta(5, 7))

# Otra forma de imprimir el resultado de la resta
resta_resultado = resta(10, 2)
print(resta_resultado)

# Función para Multiplicar
def multiplicar(x1, x2):
    resultado = x1 * x2
    return resultado

# Una forma de imprimir el resultado de la Multiplicación
print(multiplicar(5, 5))

# Una forma de imprimir el resultado de la Multiplicación
multi_resultado = multiplicar(10, 5)
print(multi_resultado)
