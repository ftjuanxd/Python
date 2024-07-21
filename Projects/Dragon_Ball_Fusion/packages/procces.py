from . import Personajes as p
from . import methods as mt

def Main():
    array = []
    while True:
        opc = mt.Menu()
        if opc == 1:
            while True:
                try:
                    name = input("Type the name of the character: ").lower()
                    speed = int(input("Type the speed of the character: "))
                    power = int(input("Type the power of the character: "))
                    energy = int(input("Type the energy of the character:"))
                    character = p.Personaje(name,speed,power,energy)
                    date = [len(array)+1,character,name,speed,power,energy]
                    array.append(date)
                    break
                except ValueError:
                    print("The speed,power and energy are value numeric") 
                except:
                    print("Mistake with the creating of the character")
        elif opc == 2:
            char1 = input("Type the name of the first Character: ")            
            char2 = input("Type the name of the first Character: ")   
            if char1 in array and char2 in array:
                print("Logro")         
            else:
                print("Nol")
        elif opc == 3:
            for i in range(len(array)):
                print(f"{i+1}.{array[i][2]}.")
            continue
        elif opc == 4:
            print("Gracias Por Jugar. XD")
            break
        else:
            print("La opcion digitada no existe intentelo otra vez. Gracias")
        mt.clear_Screen()