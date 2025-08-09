#Herencia con métodos adicionales y atributos

class Empleado:
    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

    def detalles(self):
        return f"Empleado: {self.nombre}, Edad: {self.edad}, Salario: €{self.salario}"
    

class Programador(Empleado):
    def __init__(self, nombre, edad, salario, lenguajes):
        super().__init__(nombre, edad, salario)
        self.lenguajes = lenguajes

    def detalles(self):
        return f"Programador: {self.nombre}, Edad: {self.edad}, Salario: €{self.salario}, Lenguajes: {', '.join(self.lenguajes)}"

    def agregar_lenguaje(self, lenguaje):
        self.lenguajes.append(lenguaje)


#***************************************

empleado1 = Empleado("Juan Pérez", 30, 50000)
programador1 = Programador("Ana Gómez", 32, 60000, ["Python", "JavaScript"])
print(empleado1.detalles())
print(programador1.detalles())
programador1.agregar_lenguaje("Java")
print(programador1.detalles())