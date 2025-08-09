# Funciones decoradoras
# Sirven para añadir un código extra a todas las funciones que desees, sin escribir (o copiar) manualmente el código

def funcion_decoradora(funcion_a_decorar):
    def funcion_interior():
        print("El resultado es: ")
        funcion_a_decorar()
        print("Cálculo terminado.")
        #He probado lo siguiente, pero no consigo que devuelva el valor en la misma línea
        #print(f'El resultado es: {funcion_a_decorar()}. Cálculo terminado.')
        #print(f'El resultado es: ',funcion_a_decorar(),'. Cálculo terminado.')

    return funcion_interior


@funcion_decoradora
def suma():
    print(15+20)


@funcion_decoradora
def resta():
    print(30-10)


#*****************


suma()
resta()