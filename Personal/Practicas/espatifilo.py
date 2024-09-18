phrase = ("Si, ¡El Espatifilo! es la mejor planta de todos los tiempos!","Si - !El Espatifilo! es la mejor planta de todos los tiempos!","No, !quiero una gran Estifilo!","!Espatifilo,!No ")
key = 'Espatifilo'
while True:
    p = input("Type a phrase: ")
    if p == key:
        print(phrase[0])
        break
    elif p ==key.upper():
        print(phrase[1])
        break
    elif p == key.lower():
        print(phrase[2])
    else:
        print(phrase[3]+p)
