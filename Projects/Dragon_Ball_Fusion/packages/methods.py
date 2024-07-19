import time
import os
def clear_Screen():
    #Confirma si el identificador del sistema es windows
    if os.name == "nt":
        time.sleep(2)
        os.system("cls")
    #Si no es un sistema Linux o Mac
    else:
        os.system("clear")
    
def Menu():
    while True:    
        try:
            print("\t\bDragon Ball Fusion \n1.Crear Personaje.\n2.Fusionar Personajes. \n3.Mostrar Personajes. \n4.Salir.")
            return int(input("Seleccione el numero de la opcion que quiere: "))
        except ValueError:
            print("Debe escribir un numero ")        