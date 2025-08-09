#Herencia múltiple (2 padres para 1 hijo)

class Vehiculo:
    def __init__(self, marca):
        self.marca = marca


class Motor:
    def __init__(self, tipo_motor):
        self.tipo_motor = tipo_motor


class Coche(Vehiculo, Motor):
    def __init__(self, marca, tipo_motor, modelo):
        Vehiculo.__init__(self, marca)
        Motor.__init__(self, tipo_motor)
        self.modelo = modelo

    def descripcion(self):
        return f"{self.marca} {self.modelo} con motor {self.tipo_motor}"
    

#++++++++++++

miCoche = Coche("Peugeot", "2.0", "3008")
print(miCoche.descripcion())