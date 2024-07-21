#Crea una aplicacion  que cree, fusione y muestre los personajes asi mismo el programa deber interactuar con el usuario
class Personaje:
    def __init__(self,name,speed,power,energy):
        self.name = name
        self.power = power
        self.energy = energy
        self.speed = speed
         
        
    def __add__(self,otro):
        new_name = self.name + otro.name
        speed = ((self.speed + otro.speed)/2)**1.34
        power = ((self.power + otro.power)/2)**1.34
        energy = ((self.energy + otro.energy)/2)**1.34
        return Personaje(new_name,speed,power,energy)
        