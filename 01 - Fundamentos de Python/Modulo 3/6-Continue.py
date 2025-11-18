
# Con el (for) utilizamos el rango para recorrer los elementos de la variable (element), con el primer parametro indicamos el inicio, el segundo hasta cuando, y el tercero de cuanto en cuanto
for element in range(1, 10, 1):
    # Declaramos la condición a cumplir 
    if element == 5:
        continue # Nos sirve para continuar un bucle que haya sido cortado
    print(element) # Imprimimos la variable
