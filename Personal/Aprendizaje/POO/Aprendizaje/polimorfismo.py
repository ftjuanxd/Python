class Gato():

    def sonido(self):
        return "Miau!"
    
class Perro:
    
    def sonido(self):
        return "Guau"
    
#polimorfismo de funcion

def hacer_sonido(animal):
    print(animal.sonido())
    
gato = Gato()
perro = Perro()

hacer_sonido(gato)