
# Creamos la clase (Animal)
class Animal:
    # Creamos el método (__init__) para crear el objeto
    def __init__(self, especie, edad):
        # Creamos los atributos de instancia
        self.especie = especie
        self.edad = edad

    # Método generico pero con implementación particular
    def hablar(self):
        # Método Vacío
        pass

    # Método generico pero con implementación particular
    def moverse(self):
        # Método Vacío
        pass

    # Método genérico con la misma implementación
    def describime(self):
        print("Soy un Animal del Tipo: ", type(self).__name__)


# Creamos la clase Hija (Perro)
class Perro(Animal):
    # Creamos el método (__init__) para crear el objeto
    def __init__(self, especie, edad, dueño):

        # Alternativa 1
        # self.especie = especie
        # self.edad = edad
        # self.dueño = dueño

        # Alternativa 3 - Reutilizamos el constructor de la clase padre
        super().__init__(especie, edad) # Utilizamos los atributos de la clase padre, con la función (super()), podemos reutilizar el método constructor de la clase padre
        self.dueño = dueño # Creamos el atributo (dueño)
        

# Creamos el objeto
mi_perro = Perro("Canina", 5, "Jorge")
print(mi_perro.dueño) # Imprimimos el atributo (dueño)
