# Encapsulación básica con atributos privados

"""
En Java, un atributo puede ser public, private o protected.
Python sólo tiene la opción de poner como privado, añadiendo 2 barras bajas (__)
"""

class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre
    
    #Para cambiar el valor de un atributo privado hay que usar los llamados métodos "getter" y "setter"
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_edad(self):
        return self.__edad
    
    def set_edad(self, edad):
        if edad > 0:
            self.__edad = edad
        else:
            print("Introduzca una edad positiva.")


#******************


persona1 = Persona("Ana", 35)
print(persona1.get_nombre())
print(persona1.get_edad())
persona1.set_edad(8)
print(persona1.get_edad())