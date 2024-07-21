from . import Personajes as p  # Importa tu módulo correctamente
from . import methods as mt  # Importa tu módulo correctamente

def Main():
    bd = {}
    while True:
        opc = mt.Menu()
        if opc == 1:
            while True:
                try:
                    name = input("Type the name of the character: ").lower()
                    speed = int(input("Type the speed of the character: "))
                    power = int(input("Type the power of the character: "))
                    energy = int(input("Type the energy of the character: "))
                    
                    new_character = p.Personaje(name, speed, power, energy)
                    bd[name] = new_character
                    print(f"Character created: {new_character}\n")
                    break
                except ValueError:
                    print("The speed, power, and energy must be numeric values.") 
                except Exception as e:
                    print(f"Error creating the character: {e}")
        
        elif opc == 2:
            # Mostrar personajes almacenados
            print("Characters stored:")
            for name, character in bd.items():
                print(character)
        
        elif opc == 3:
            # Combinar dos personajes
            name1 = input("Enter the name of the first character to combine: ").lower()
            name2 = input("Enter the name of the second character to combine: ").lower()

            if name1 in bd and name2 in bd:
                combined_character = bd[name1] + bd[name2]
                bd[combined_character.name] = combined_character
                print(f"Combined character created: {combined_character}\n")
            else:
                print("One or both character names are not in the database.")

        elif opc == 0:
            # Salir del programa
            break

        else:
            print("Invalid option. Please choose again.")
