
# Creamos la clase (Animal)
class Animal:
    # Creamos el método (__init__) para crear el objeto
    def __init__(self, especie, edad):
        # Creamos los atributos de instancia
        self.especie = especie
        self.edad = edad

    # Método genérico pero con implementación particular
    def hablar(self):
        # Método Vacío
        pass

    # Método genérico pero con implementación particular
    def moverse(self):
        # Método Vacío
        pass

    # Método genérico con la misma implementación
    def describeme(self):
        print("Soy un Animal del Tipo", type(self).__name__)


# Creamos la Clase Hija (Perro)
class Perro(Animal):
    # Creamos el método hablar()
    def hablar(self):
        print("Guau!")

    # Creamos el método moverse()
    def moverse(self):
        print("Caminando con 4 patas")


# Creamos la Clase Hija (Vaca)
class Vaca(Animal):
    # Creamos el método hablar()
    def hablar(self):
        print("Muuu!")

    # Creamos el método moverse()
    def moverse(self):
        print("Caminando con 4 patas")


# Creamos la Clase Hija (Abeja)
class Abeja(Animal):
    # Creamos el método hablar()
    def hablar(self):
        print("Bzzz")

    # Creamos el método moverse()
    def moverse(self):
        print("Volando")

    # Creamos un Nuevo Método 
    def picar(self):
        print("Picar!")


# Creamos los objetos 
mi_perro = Perro("Mamifero", 10)
mi_vaca = Vaca("Mamifero", 23)
mi_abeja = Abeja("Insecto", 1)

# Llamamos los métodos
mi_perro.hablar()
mi_vaca.hablar()

mi_vaca.describeme()
mi_abeja.describeme()

mi_abeja.picar()

# Métodos heredados por la clase padre
print(mi_perro.edad)
print(mi_perro.especie)
