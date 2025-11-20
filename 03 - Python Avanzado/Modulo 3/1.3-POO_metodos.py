
# Creamos la clase (Perro)
class Perro:
    # Atributo de Clase
    especie = "Mamifero"

    # El método (__init__) es llamado al crear el objeto
    def __init__(self, nombre, raza):
        print(f"Creando Perro {nombre}, {raza}")

        # Atributos de Instancia
        self.nombre = nombre
        self.raza = raza

    # Creamos el método (ladra)
    def ladra(self):
        print("Guau")

    # Creamos el método (camina)
    def camina(self, pasos):
        print(f"Caminando {pasos} pasos")

# Creamos el objeto (mi_perro)
mi_perro = Perro("Toby", "Bulldog")
mi_perro.ladra()
mi_perro.camina(10)


# Ejemplo Alumno
print("-----Ejemplo 1-----")

# Creamos la clase (Alumno)
class Alumno:
    # Creamos el método (__init__) para crear el objeto
    def __init__(self, nombre, apellido, edad):
        # Creamos los atributos de instancia
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    # Creamos el método (rendir_examen)
    def rendir_examen(self):
        print("Tomando Examen en Aula")

    # Creamos el método (asistir)
    def asistir(self):
        print("Asistiendo Puntual")

# Creamos el objeto (Alumno_1)
alumno_1 = Alumno("Jorge", "Villavicencio", 25)

# Imprimimos los atributos
print(alumno_1.nombre)
print(alumno_1.apellido)
print(alumno_1.edad)

# Llamamos a los métodos
alumno_1.rendir_examen()
alumno_1.asistir()
