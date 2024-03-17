import operaciones as calc

Number=[]

print("----------------------------------")
print("Bienvenido A la Calculdora Zone.\n")
print("----------------------------------")
print("Que Operaciones de Desea Realizar.")
print("1.Suma 2.Resta 3. Multiplicación 4.División 5.Potencia")

opc = int(input("Digite el numero de la operacion que desea hacer."))

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
