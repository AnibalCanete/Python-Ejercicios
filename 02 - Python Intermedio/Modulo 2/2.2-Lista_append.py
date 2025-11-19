
# El (append()) sirve para agregar elementos a una lista
lista = [1, 2] # Creamos una lista con números
listaAuxiliar = ["Jorge", "Hola"] # Creamos una lista con caracteres
print(lista) # Imprimimos la variable (lista)

print("-----Lista Sin Agregar Ningun Elemento-----") #Imprimimos una linea que nos sirva para separar la antigua lista de la nueva

lista.append(listaAuxiliar)
print(lista)

print("-----Lista con un Nuevo Elemento Agregado-----") #Imprimimos una linea que nos sirva para separar la lista nueva de la anterior

print("------Ejercicio de Demostración------")

lista2 = [1, 2] # Creamos la variable (lista2)
print(lista2) # Imprimimos la variable (lista2)

print("-----Lista Sin Agregar Ningun Elemento-----") #Imprimimos una linea que nos sirva para separar la lista anterior de la nueva

lista2.append(3) # Agregamos un nuevo elemento a la variable (lista2) con el (append())
print(lista2) # Imprimimos la variable (lista2) con su nuevo elemento

print("-----Lista con un Nuevo Elemento Agregado-----")
