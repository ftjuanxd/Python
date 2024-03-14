#creando listas
frutas = ["bananas","granada","ciruela","pera","sandia"]
cadena = "Hijastro ."
numeros = [1,2,3,4]

#evitando que se coma una granada con la sentencia continue
for fruta in frutas:
    if fruta == 'granada':
        #salta a la siguiente iteracion
        continue
    print(f'Me voy a comer {fruta}')
    
print("\n")   
#evitar que el bucle siga ejecutandose    
for fruta in frutas:
    print(f'Me voy a comer {fruta}')
    if fruta == 'pera':
        #termina el bucle y tampoc ejecuta el else
        break
else:
    print("bucle terminado")
    
#recorrer una cadenade texto
for letra in cadena:
    print(letra)
    
#for en una sola linea de codigo(duplicamos los numeros)
numeros_duplicados = [x*2 for x in numeros]#expresion matetamtica primero despues el bucle
print(numeros_duplicados)