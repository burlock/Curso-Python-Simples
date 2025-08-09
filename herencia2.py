class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def descripcion(self):
        #f vale para dar formato a la salida retornada
        return f"{self.marca} {self.modelo}"
    
    def tipo(self):
        #Con 'pass' estoy permitiendo que dicho método quede vacío, a expensas de ser sobreescrito en clases hijas
        pass
    
class Coche(Vehiculo):
    #Debo traerme todos los atributos del padre para el constructor del hijo (ej. quito 'modelo'). Sólo los que interesan
    def __init__(self, marca, modelo, num_puertas):
        super().__init__(marca, modelo)
        self.num_puertas = num_puertas

    #Heredo y sobreescribo un método
    def tipo(self):
        return "Es un coche."
    

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, tipo_bici):
        super().__init__(marca, modelo)
        self.tipo_bici = tipo_bici

    def tipo(self):
        return "Es una bicicleta."
    
    

#Creo una instancia de Coche
miCoche = Coche("Peugeot", "3008", 5)
miBici = Bicicleta("BH", "Rapide", "Carretera")

#Muestro atributos y métodos
print(miCoche.descripcion(), "-", miCoche.tipo())
print(miBici.descripcion(), "-", miBici.tipo())