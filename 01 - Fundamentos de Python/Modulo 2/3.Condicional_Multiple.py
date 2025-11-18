
# Condicional Multiple
# Declaramos la variable (n) y utilizamos un (input) para introducir un valor
n = int(input("Ingrese un Número: "))

# Con el (if) declaramos la condición que debe cumplirse, el valor de (n) es mayor que (0)
if n > 0:
    print("Ingresaste un Número Positivo")
# Con el (elif) declaramos la otra condición puede cumplirse, el valor de (n) es menor que (0)
elif n < 0:
    print("Ingresaste un Número Negativo")
# Con el (else), declaramos que hacer en caso de que ninguna de las otras condiciones se cumplan
else:
    print("Ingresaste Cero")
