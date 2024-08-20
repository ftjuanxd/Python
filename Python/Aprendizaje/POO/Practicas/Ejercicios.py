import os

def clean_Screen():
    if os.name == 'nt': #Si es windows
        os.system_clean('cls')
    else:#si el sistema operativo es macOs o Linux
        os.system_clean('clear')

class Persona:
    
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad =  edad
        
    def imp_Per(self):
        print(f"Your name is: {self.nombre}\n Your age is: {self.edad} ")

class Estudiante(Persona):
    
    def __init__(self,nombre,edad,grado):
        super().__init__(nombre,edad)
        self.grado = grado
    
    def imp_Est(self):
        print(f"Your grade is:{self.grado}")

while True:
    try:
        nombre = input("Type your name: ")        
        edad = int(input("Type your age: "))
        grado = input("Type your grade:")
        break
    except ValueError:
        print("The age are numbers not characters")
        
est = Estudiante(nombre,edad,grado)
while True:
    try:  
        clean_Screen()
        opc = int(input("\tMenu\n1.Show Student Data \n2.Show Grade"))
        if opc == 1:
            est.imp_Per()
        elif opc == 2:
            est.imp_Est()
        else:
            print("Just There Are Two Opcions. Stupid")
            continue
        break
    except ValueError:
        print("Just Numbers. Asshole")
