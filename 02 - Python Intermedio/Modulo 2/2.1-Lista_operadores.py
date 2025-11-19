
# Lista con Operadores
# Sumatoria 
padres = ["Mamá", "Papá"]
abuelos = ["Abuelo", "Abuela", "Hijos"]
numeros = [1, 2, 3]
familia = numeros + abuelos + padres # Creamos la variable (familia) donde sumamos las listas para crear una sola lista
print(familia) # Imprimimos la variable (familia)

print("--------------------------------------") #Imprimimos una linea que nos sirva para separar los diferentes tipos de metodos

# Multiplicación
lista_numeros = [1, 2, 3, 4, 5] * 2 # Con la multiplicación lo que hacemos en realidad es duplicar la lista (lita_numeros)
print(lista_numeros) # Imprimimos la lista (lista_numeros)

print("--------------------------------------") #Imprimimos una linea que nos sirva para separar los diferentes tipos de metodos

# IN
lista = ["Juan", "Luis", "Almendra", "Jorlan", "Maria", "Luisa"]
print("Juan" in lista) # Imprimimos un resultado (Verdadero/True), si el valor que introducimos se encuentra en la lista 
print("Pedro" in lista) # Imprimimos un resultado (Falso/False), si el valor que introducimos no se encuentra en la lista

print("--------------------------------------") #Imprimimos una linea que nos sirva para separar los diferentes tipos de metodos

# NOT IN
lista = ["Juan", "Luis", "Almendra", "Jorlan", "Maria", "Luisa"]
print("Juan" not in lista) # Imprimimos un resultado (Falso/False), si el valor introducido se encuentra en la lista
print("Pedro" not in lista) # Imprimimos un resultado (Verdadero/True), si el valor introducido no se encuentra en la lista
