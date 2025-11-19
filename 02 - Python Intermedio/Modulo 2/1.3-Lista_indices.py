
# Positivos
# Creamos la lista (dias)
dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

print("Valor que se encuentra en el indice 1:", dias[1]) # Con un solo valor indicamos el elemento que se encuentra en esa posición
print("Valores que se encuentran desde el indice inicial 0 hasta 2:", dias[:3]) # Con los puntos dobles (:) seguido del valor indicamos hasta que posición se recortara la lista
print("Valores que se encuentran desde el indice 3 hasta 6 que es el indice final:", dias[3:]) # Cuando indicamos el valor seguido de los puntos dobles (:), indicamos desde que elemento inicia el recorte
print("Valores desde el indice 3 hasta el indice 4:", dias[3:5]) # Cuando utilizamos dos valores, con uno indicamos su inicio y el otro su final, en este caso seria desde el elemento (3) hasta el elemento (5)

print("----------------------") #Imprimimos una linea que nos sirva para separar los diferentes tipos de metodos

# Negativos
# Creamos la lista (dias)
dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

print("Valor que se encuentra en el indice ultimo 6:", dias[-1]) # Cuando utilizamos numeros negativos estariamos iniciando el recorrido desde la derecha hacia la izquierda
print("Valor que se encuentra en el indice 3:", dias[-5]) # En este caso obtendriamos el elemento (Miercoles)
print("Valor que se encuentra en el indice 4:", dias[-3]) # En este caso obtendriamos el elemento (Viernes)
print("Valores que se encuentran desde el indice 4 hasta 6 que es el indice final:", dias[-3:]) # Tambien podemos hacer recoertes desde la derecha, en este caso, empezaria desde el elemento (Viernes) hasta el ultimo elemento

print("----------------------") #Imprimimos una linea que nos sirva para separar los diferentes tipos de metodos

# Utilizando Len
# Creamos la lista (dias)
dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

print("Cantidad de Elementos:", len(dias)) # Imprimimos la cantidad de elementos de la lista (dias)
print(dias[len(dias)-1]) # Imprimimos el ultimo elemento de la lista (dias)
