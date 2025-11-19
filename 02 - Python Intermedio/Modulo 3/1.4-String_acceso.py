
palabra = "Bienvenidos a Python" # Creamos la variable (palabra)

print(palabra[4]) # Si queremos imprimir por indice, colocamos entre corchetes ([]) el valor del elemento que queremos imprimir
print(palabra[:6]) # Tambien podemos imprimir por recortes, en este caso, desde el elemento (0) hasta el elemento (5), es un valor menos por que se cuenta desde el cero no desde el uno
print(palabra[6:10]) # En este caso, imprimimos desde el elemento (6) hasta el elemento elemento (9)
print(palabra[10:]) # En este caso, imprimimos desde el elemento (10) hasta el ultimo elemento
print("Resultado") # Imprimimos un Titulo
print(palabra[:6] + palabra[6:10] + palabra[10:]) # En este caso, concatenamos diferentes recortes y imprimimos el resultado

