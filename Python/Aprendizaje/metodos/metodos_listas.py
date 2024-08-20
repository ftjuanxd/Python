#se utiliza para crear listas vacias
lista = list([1,5,32,False,5,3,2,2,True ])

#devuelve cantidad de elementos de la lista
resultado = len(lista)

#agregando elementos a la lista
lista.append(16)

#agregando un elemento a la lista en un indice especifico
lista.insert(3,"toma chamaco")

#agregando varios elementos a la lista, pero no le pasamos los parametros sueltos sino que se encuentren en una lista
lista.extend([True,2006])

#eliminando un elemento de la lista (por su indice) si escribrimos el -1 nos elimina el ultimo dato de la lista
lista.pop(-1)#-1 para eliminar el ultimo -2 para eliminar el antepenultimo y asi sucesivamente

#removiendo un elemento de la lista por su valor
lista.remove("toma chamaco")

#eliminando todos los elementos de la lista
#lista.clear()
# ordena de manera ascendente la lista solo funciona con numeros entero, flotantes y booleanos
#si se usa el parametro reverse ordenaen revarsa
lista.sort()
#lista.sort(reverse=True)

#inviertiendo los parametros de una 
#lista.reverse()

#verificando si un numero esta en la lista
elemento_encontrado = lista.index(16)

print (elemento_encontrado)