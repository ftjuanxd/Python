from . import Personajes as p
from . import methods as mt

def Main():
    pj = p.Personaje()
    while True:
        opc = mt.Menu()
        if opc == 1:
            pj.Crear_Personaje()            
        elif opc == 2:
            while True:
                name1 = input("\nEscriba el nombre del primer personaje: ")
                if pj.mostrar_personaje(name1) == False:
                    print("El nombre digitado no existe dentro de la base de datos. Intentalo Nuevamente.")
                    continue
                name2 = input("\nEscriba el nombre del Segundo personaje: ")
                if pj.mostrar_personaje(name2) == False:
                    print("El nombre digitado no existe dentro de la base de datos. Intentalo Nuevamente.")
                    continue
                nuevo = pj.personaje[name1] + pj.personaje[name2]
                pj.mostrar_personaje(nuevo)
                break
        elif opc == 3:
            if pj.mostrar_personaje() == {}:
                print("No hay Personajes")
            else:
                print(pj.mostrar_personaje())
        elif opc == 4:
            print("Gracias Por Jugar. XD")
            break
        else:
            print("La opcion digitada no existe intentelo otra vez. Gracias")
            continue
        mt.clear_Screen()