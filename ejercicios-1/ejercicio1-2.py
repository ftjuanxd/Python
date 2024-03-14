#le pedimos los datos al usuario
frase =input("decime algo maestro, y te calculo cuanto te demora en decirlo: ")

palabras_separadas= frase.split(" ")

cantidad_de_palabras = len(palabras_separadas)

if cantidad_de_palabras > 120:
        print("Para flaco tampoco te pedi un testamento")

print(f'Dijiste {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras/2} segundos en decirlo')

print(f'Dalto lo diria en {cantidad_de_palabras *100 // 2 * 0.3/ 10} segundos')
