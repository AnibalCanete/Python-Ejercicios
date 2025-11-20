
# Defnimos una clase Padre
class Animal:
    pass

# La herencia nos permite que la clase hija pueda heredas los métodos y atributos de la clase padre 

# Creamos una clase hija que hereda de la del padre
class Perro(Animal): # Colocando entre los parentesis el nombre de la clase padre, la clase hija puede heredar los métodos y atributos de la clase padre
    pass

print(Perro.__bases__) # Utilizamos (__bases__) para saber las bases de la clase (Perro)

print(Animal.__subclasses__()) # Utilizamos (__subclasses) para conocer las sub clases o clases hijas de la clase (Animal)
