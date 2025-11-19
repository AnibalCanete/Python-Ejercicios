
# Ejercicio 1 - Crea una Lista de nombres y agrega el nombre (Felipe)
nombres = ["Jorge", "Luis", "Juan", "Harumi"]
nombres.append("Felipe")
print(nombres)

# Ejercicio 2 - Crea la variable (cadena) y escribe el valor ("soy una cadena de TEXTO") y convierte todo el valor en mayusculas
cadena = "soy una cadena de TEXTO"
print(cadena.upper())

# Ejercicio 3 - Crea una función llamada (Calculadora), que nos permita sumar, restar, multiplar y nos de la potencia
def Calculadora(x, y, z):
    suma = x + y + z
    resta = x - y - z
    multiplicacion = x * y * z
    potencia = pow(x, y)
    return suma, resta, multiplicacion, potencia

print(Calculadora(10, 2, 5))
