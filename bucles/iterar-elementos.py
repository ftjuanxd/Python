animales = ("gato","perro","loro","cocodirlo","pez")
numeros = (1,2,3,4,45)
#recorriendo la lista animales
for animal in animales:
    print(f'Ahora la variable anial es igual a: {animal}')

#recorriendo la lista numeros y multiplicando cada valor por 10
for numero in numeros:
    resultado = numero *40
    print(resultado)
#iterando dos llistas del mismo tamaño y al mismo tiempo
for numero,animal in zip(animales,numeros):
    print(f"recorriendo lista 1: {numero}")
    print(f"recorriendo lista 1: {animal}")

#range  se trabaja con minimo un valor si se le pasa uno solo iniciara desde cero hasta el valor dato en caso de dar dos el primero sera el parametro de inicio y el segundo el de final -1    
for num in range(1,5):
    print(f"Numero:{num}")

#forma no optima de recorrer una lista(no funciona con conjuntos)
for num in range(len(numeros)):
    print(numeros[num])
    
#forma correcta de recorrer una lista con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"El indice es [{indice}] y el valor es: {valor}")
    
#usando el for/else 
for numero in numeros:
    print(f"Ejecutando el ultimo bucle, valor actual: {numero} ")
else:
    print("El bucle termino")
#todo lo anterior funciona exactamente igual para tuplas y conjuntos