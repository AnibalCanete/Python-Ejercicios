
# Funciones con parametros por defecto
def area_circulo(radio, pi=3.14):
    area = pi*pow(radio, 2)
    return area

print(area_circulo(2)) # Podemos solo enviar un parametro, ya que el segundo tiene su valor por defecto, es decir, no hace falta que incluyamos el segundo parametro

print(area_circulo(2, 3.1415)) # Tambien podemos introducir un segundo valor pero utilizaria ese valor en el calculo y no el que tiene por defecto, ocasionando que el resultado varie
