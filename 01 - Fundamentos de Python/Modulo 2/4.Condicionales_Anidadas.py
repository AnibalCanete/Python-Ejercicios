
# Condicional Anidada
# Declaramos la variable (edad) y utilizamos un (input) para introducir un valor
edad = int(input("Ingresar Edad: "))

# Con el (if), declaramos la condición que debe cumplirse
if edad >= 18:
    print("Mayor de Edad")
# Con el (else), establecemos que hacer en caso de que no se cumpla la condición
else:
    # Con el (if), declaramos la condición que debe cumplirse
    if edad > 0:
        print("Menor de Edad")
    # Con el (else), establecemos que hacer en caso de que no se cumpla la condición
    else: 
        print("Edad no es Correcta")
