
# Creamos la clase padre (Animal)
class Animal:
    # Creamos el método (__init__) que sirve para crear el objeto
    def __init__(self, especie, edad):
        # Creamos los atributos de instancia
        self.especie = especie
        self.edad = edad

    # Método Genérico pero con Implementación Particular
    def hablar(self):
        # Método Vacío
        pass

    # Método Genérico per con Implementación Particular
    def moverse(self):
        # Método Vacío
        pass

    # Método Genérico con la Misma Implementación
    def describime(self):
        print("Soy un Animal del Tipo:", type(self).__name__)


# Creamos la clase hija (Mamifero)
class Mamifero(Animal):
    def __init__(self, especie, edad):
        super().__init__(especie, edad)

# Creamos la clase hija (Perro), que es hija de la clase (Mamifero)
class Perro(Mamifero): # La clase (Perro) es hijo de (Mamifero) pero por herencia multiple, (Perro) hereda lo que tenga la clase (Animal)
    def __init__(self, especie, edad, dueño):
        super().__init__(especie, edad)
        self.dueño = dueño

# Creamos el Objeto
mi_perro = Perro("Toby", "Bulldog", "Jorge")

# Llamamos a los métodos
mi_perro.describime()
