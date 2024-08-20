#le pedimos los datos al usuario
#frase =input("decime algo maestro, y te calculo cuanto te demora en decirlo: ")

def time_word(frase):
        palabras_separadas= frase.split(" ")

        cantidad_de_palabras = len(palabras_separadas)

        #Dalto_seg= round(cantidad_de_palabras / 2 * 0.3 * 10,2)

        if cantidad_de_palabras > 120:
                print("Para flaco tampoco te pedi un testamento")

        print(f'Dijiste {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras/2} segundos en decirlo')

        #print(f'Dalto lo diria en {Dalto_seg} segundos')