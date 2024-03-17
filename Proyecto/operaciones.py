def Solicitar_Numeros():
    lista = []
    opc = ""
    while opc != "N" and opc != "n":
        num=int(input("Digite un Numero:"))
        lista.append(num)
        opc = input("Desea ingresar mas numeros. S/N") 
    return lista
def Suma(lista):
    suma = list()
    if len(lista) ==0 :
        return lista
    elif len(lista) == 2:
        suma =lista[0]+lista[1]
    else:
        for i in lista:
            suma += lista
    return print(f"Suma:{suma}") 

def Resta(lista):
    resta = int()
    if len(lista) ==1 :
        return lista
    elif len(lista) == 2:
        resta =lista[0]-lista[1]
    else:
        for i in lista:
            resta -= lista
    return print(f"Resta:{resta}") 

def Division(lista):
    division=int()
    if len(lista) ==1 :
        return lista
    elif len(lista) == 2:
        division =lista[0]//lista[1]
    else:
        for i in lista:
            division //= lista
    return print(f"Division:{division}") 

def Multiplicacion(lista):
    multiplicacion=int()
    if len(lista) == 1 :
        return lista
    elif len(lista) == 2:
        multiplicacion =lista[0]*lista[1]
    else:
        for i in len(lista):
            multiplicacion *= lista[i]
    return print(f"Multiplicacion:{multiplicacion}") 

def Potencia(lista):
    potencia=int()
    if len(lista) == 1 :
        return lista
    elif len(lista) == 2:
        potencia =lista[0]**lista[1]
    else:
        for i in len(lista):
            potencia **= lista[i]
    return print(f"Potencia: {potencia}")
