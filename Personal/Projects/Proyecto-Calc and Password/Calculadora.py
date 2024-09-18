import operaciones as calc

lip=str()

while lip != "N" and lip != "n":

    Number=[]
    opc = calc.Menu()

    if opc == 1:
        #Inicializamos la lista number y Realizamos el llamado de la funcion Suma
        Number = calc.Solicitar_Numeros()
        calc.Suma(Number)

    elif opc == 2:
        
        Number = calc.Solicitar_Numeros()
        calc.Resta(Number)

    elif opc == 3:
        Number = calc.Solicitar_Numeros()
        calc.Multiplicacion(Number)

    elif opc == 4:
        Number = calc.Solicitar_Numeros()
        calc.Division(Number)
    elif opc == 5:
        Number = calc.Solicitar_Numeros()
        calc.Potencia(Number)
    else:
        print("La operacion selecionada no existe.")
    
    Number.clear()
    lip = input("Desea Seguir Utilizando la Calculadora del Futuro. S/N") 
    calc.Clean()