
# Creamos el diccionario (d), con sus respectivos valores
d = {
    "A": 1,
    "B": 2
}

print(d.get("A")) # Con la función (get()), podemos obtener el valor de la clave ("A") que estamos solicitando 
# En el caso de que no exista la clave en el diccionario, podemos tener un mensjae por defecto, para que nos de dicho mensaje como resultado
print(d.get("Z", "No Encontrado")) 
