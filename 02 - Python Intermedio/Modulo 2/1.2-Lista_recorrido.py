
# Creamos la lista (dias)
dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

print("Utilizando For") # Imprimimos un Titulo
for item in dias: # Con el (For) utilizamos la variable (item) para recorrer los elementos de la lista (dias)
    print(item) # Imprimimos la variable (item) para visualizar los valores de la lista

print("----------------------") #Imprimimos una linea que nos sirva para separar los diferentes tipos de metodos

print("Utilizando Range") # Imprimimos un Titulo
for i in range(len(dias)): # Con el (for) utilizamos la variable (i) para cargar los elementos de la lista, con el (range) recorremos el rango, utilizando la función (len) obtenemos el tamaño de la lista
    print(dias[i]) # Imprimimos la lista con sus respectivos elementos en la variable (i)

print("----------------------") #Imprimimos una linea que nos sirva para separar los diferentes tipos de metodos

print("Utilizando enumerate") # Imprimimos un Titulo
for i, item in enumerate(dias): # Con el (for), declaramos dos variables, la primera indica en que posicion se encuentra el elemento y la segunda seria el valor del elemento, con el (enumerate) indicamos la lista (dias)
    print(i, item) # Imprimimos la lista con los valores de la variable (i) y los valores de la variable (item)

