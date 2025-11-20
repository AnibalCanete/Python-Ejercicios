
class Perro: 
    # El método (__init__) es llamado al crear el objeto
    def __init__(self, nombre, raza, edad):
        print(f"Creando Perro {nombre}, {raza}")

        # Atributos de Instancia
        self.nombre = nombre
        self.raza = raza
        self.edad = edad

mi_perro = Perro("Toby", "Bulldog", 5) # Creamos el perro, Toby, Bulddog, 5
print(type(mi_perro)) # Imprimimos el tipo de dato

# Para imprimir los atributos, colocamos el nombre del objeto (mi_perro) seguido de un punto y el nombre del atributo (.nombre)
print(mi_perro.nombre) # Imprimimos el nombre
print(mi_perro.raza) # Imprimimos la raza
print(mi_perro.edad) # Imprimimos la edad


# Ejemplo Alumno
print("-----Ejemplo 1-----")

# Creamos la clase (Alumno)
class Alumno:
    # Creamos el método (__init__) para crear el objeto
    def __init__(self, nombre, apellido, edad):
        # Declaramos los atributos de instancia
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

# Creamos un Alumno 
alumno_1 = Alumno("Jorge", "Villavicencio", 25)
# Imprimimos los Atributos
print(alumno_1.nombre)
print(alumno_1.apellido)
print(alumno_1.edad)


# Ejemplo Auto
print("-----Ejemplo 2-----")

# Creamos la clase (Auto)
class Auto:
    # Creamos la función (__init__) para crear el objeto
    def __init__(self, marca, color, modelo):
        # Creamos los atributos de instancia
        self.marca = marca
        self.color = color
        self.modelo = modelo

# Creamos Tres Objetos
Auto_1 = Auto("Toyota", "Rojo", "Supra")
Auto_2 = Auto("Toyota", "Blanco", "Vitz")
Auto_3 = Auto("Toyota", "Negro", "Noah")

# Imprimimos los atributos del objeto (Auto_1)
print(Auto_1.marca)
print(Auto_1.color)
print(Auto_1.modelo)

print("------------------------------") #Imprimimos un linea divisioria, para visualizar mejor los resultados

# Imprimimos los atributos del objeto (Auto_2)
print(Auto_2.marca)
print(Auto_2.color)
print(Auto_2.modelo)

print("------------------------------") #Imprimimos un linea divisioria, para visualizar mejor los resultados

# Imprimimos los atributos del objeto (Auto_3)
print(Auto_3.marca)
print(Auto_3.color)
print(Auto_3.modelo)
