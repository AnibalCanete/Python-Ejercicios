
# Ejercicio 1
# Indica el Resultado de la Variable Suma
print("----------Ejercicio 1----------")
matriz = [
    [1, 2], [3, 4], [5, 6],
    [7, 8], [9, 10], [11, 12], 
    [13, 14], [15, 16], [17, 18], 
    [19, 20], [21, 22]
]

suma = 0

for x in range(len(matriz)):
    suma += x
    print(x)

# Ejercicio 2 
# Indicar cuáles son los valores que se muestran en consola luego de ejecutar las siguientes lineas de código
print("----------Ejercicio 2----------")
x = ("11", "uno", 1, "1", 1.0, 1, 10)
print(x.count(1))
print(x.count("1"))

# Ejercicio 3 
# Dada las siguientes variables, indica cuáles son los resultados correctos.
print("----------Ejercicio 3----------")
d1 = dict(
    Nombre="Jorge",
    Edad=16,
    Nota=10.7
)

d2 = dict([
    ("Nombre", "Jorge"),
    ("Edad", 15),
    ("Nota", 17)
])

print(d1["Nota"] + d2["Nota"])
