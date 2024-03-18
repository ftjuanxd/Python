import os

def Clean():
    # Limpiar la pantalla
    os.system('cls' if os.name == 'nt' else 'clear')

def Menu():
    opc = 0
    print("----------------------------------")
    print("Bienvenido A la Calculdora Zone.\n")
    print("----------------------------------")
    print("Que Operaciones de Desea Realizar.")
    print("1.Suma 2.Resta 3. Multiplicación 4.División 5.Potencia")

    opc = int(input("Digite el numero de la operacion que desea hacer: "))
    return opc

def Solicitar_Numeros():
    lista = []
    opc = ""
    while opc != "N" and opc != "n":
        num=int(input("Digite un Numero:"))
        lista.append(num)
        opc = input("Desea ingresar mas numeros. S/N") 
    return lista

def Suma(lista):
    suma = 0
    if len(lista) != 0 :
        for i in lista:
            suma += i
    else: 
        suma = lista[0]
    return print(f"Suma:{suma}") 

def Resta(lista):
    resta = 0
    if len(lista) != 0 :
        for i in lista:
            resta -= i
    else:
        resta = lista[0]
        
    return print(f"Resta:{resta}") 

def Division(lista):
    division=0
    r =0
    if len(lista) != 0 :
        for i in lista:
            if i == lista[0] and r == 0:
                division = i
                r =1
            else:
                division //= i
    else:
        division = lista[0]           
        
    return print(f"Division:{division}") 

def Multiplicacion(lista):
    multiplicacion=1
    if len(lista) != 0 :
        for i in lista:
            multiplicacion *= i
    else:
        multiplicacion = lista[0]
        
    return print(f"Multiplicacion:{multiplicacion}") 

def Potencia(lista):
    potencia=0
    r = 0
    if len(lista) != 0 :
        for i in lista:
            if i == lista[0] and r == 0:
                potencia = i
                r =1
            else:
                potencia **= i
    else:
        potencia = lista[0]
        
    return print(f"Potencia: {potencia}")
