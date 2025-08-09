class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def arrancar(self):
        return "El vehículo se ha arrancado satisfactoriamente."
    
    def parar(self):
        return "El vehículo se ha parado."
    
class Coche(Vehiculo):
    #Puedo no traerme todos los atributos del padre para el constructor del hijo (ej. quito 'modelo'). Sólo los que interesan
    def __init__(self, marca, modelo, num_puertas):
        super().__init__(marca, modelo)
        self.num_puertas = num_puertas

    def abrir_puertas(self):
        return f"Abriendo {self.num_puertas} puertas."
    

#Creo una instancia de Coche
miCoche = Coche("Peugeot", "3008", 5)

#Muestro atributos y métodos
print(miCoche.marca)
print(miCoche.arrancar())
print(miCoche.num_puertas)
print(miCoche.abrir_puertas())