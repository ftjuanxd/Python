class Animal:
    
    def comer(self):
        print("Como")
        
class Mamifero(Animal):
    
    def amamantar(self):
        print("amamantar")
        
class Ave(Animal):
    
    def volar(self):
        print("Volar")
    
class Murcielago (Mamifero,Ave):
    pass

murcielago = Murcielago()

murcielago.comer()
murcielago.amamantar()
murcielago.volar()