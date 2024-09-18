import random

upper_limit = 100
down_limit = 0
opc = True
number = random.randint(down_limit,upper_limit)
while opc:
    try:
        number_user =int(input("Adivine el numero: "))
    except Exception :
        print('Intentalo otra vez.')
        print(number)
    else:
        if number!= number_user:
            print("Incorecto Sigue intentando.")
        else:
            print("Adivinaste el numero, Felicidades.")
            opc = False

