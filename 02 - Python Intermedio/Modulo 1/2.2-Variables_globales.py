
# Una variable global es la que se puede utilizar en todo el proyecto o en todo el programa que estamos realizando
# Creamos la variable global (PI)
PI = 3.1415

# Creamos la función (area_circulo)
def area_circulo(radio):
    area = PI*pow(radio, 2)
    return area # Retornamos el valor de la variable (area)

radio = float(input("Radio: ")) # Creamos la variable (radio), con un tipo de dato (float/flotante, es decir, en decimales) y utilizamos un (input) para introducir un valor
resultado = area_circulo(radio) # Creamos la variable (resultado) y utilizamos la función (area_circulo), con el valor de la variable (radio) 
print("El Area del Circulo con Radio {} es {} ".format(radio, resultado)) # Imprimimos el radio y el resultado del area de nuestro circulo
