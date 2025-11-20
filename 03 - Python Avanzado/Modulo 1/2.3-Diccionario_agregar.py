
# Creamos el diccionario 
d1 = {
    "Nombre": "Juan",
    "Edad": 24,
    "Documento": 10203040
}

print(d1) # Imprimimos el diccionario antes de agregar un elemento nuevo
# Colocamos el nombre del diccionario, entre corchetes ([]) escribimos la nueve clave a agregar ("Apellido"), seguido del valor ("Lopez") de la nueva clave
d1["Apellido"] = "Lopez" 
d1["Telefono"] = 984556677 # En este caso, agregariamos la clave (["Telefono"]), con su valor ("984556677")
d1[90] = "Horario" # Tambien podemos agregar una clave de tipo entero
print(d1) # Imprimimos el diccionario despues de agregar los nuevos elementos
