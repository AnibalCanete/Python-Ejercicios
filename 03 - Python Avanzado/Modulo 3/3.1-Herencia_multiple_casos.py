
# Creamos la clase padre (Clase1)
class Clase1:
    pass

# Clase Hija (Clase2) - Hijo de la Clase1
class Clase2(Clase1):
    pass

# Clase Hija (Clase3) - Hijo de la Clase2 - Tambien es hijo de la Clase1
class Clase3(Clase2):
    pass

print(Clase3.__mro__) # Con (__mro__) podemos visualizar todas las relaciones que tiene la (Clase3)

