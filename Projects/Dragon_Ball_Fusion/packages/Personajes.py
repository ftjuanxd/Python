#Crea una aplicacion  que cree, fusione y muestre los personajes asi mismo el programa deber interactuar con el usuario
class Personaje:
    def __init__(self):
        self.personaje = {}

    def Crear_Personaje(self):
        while True:
            try:
                name = input("Type the name of the character: ")
                speed = int(input("type the speed of the character: "))
                power = int(input("Type the power of the character: "))
                energy = int(input("Type the energy of the character: "))
                self.personaje[name] = {"Speed":speed,"Power":power,"Energy":energy}
                print("El Personaje ha sido creado.")
                break
            except ValueError as e:
                print(type(e),e)
    
    def mostrar_personaje(self,name=""):
        if name != "":
            if name in self.personaje:
                return f"Name: {name}",self.personaje[name]
            else:
                return False
        else:
            return self.personaje
        
    def __add__(self,name1,name2):
        new_name = name1 + name2
        speed = ((self.personaje[name1]["Speed"] + self.personaje[name2]["Speed"])/2)**1.34
        power = ((self.personaje[name1]["Power"] + self.personaje[name2]["Power"])/2)**1.34
        energy = ((self.personaje[name1]["Energy"] + self.personaje[name2]["Energy"])/2)**1.34
        self.personaje[new_name] =  {"Speed":speed,"Power":power,"Energy":energy}