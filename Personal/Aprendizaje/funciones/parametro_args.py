#forma no optima de sumar valores
# def suma(lista):
#     numeros_sumados = 0
#     for numero in lista:
#         numeros_sumados=numeros_sumados + numero
#     return numeros_sumados        
# resultado = suma([5,5,5,5,5,23,16])
#
#utilizando el operador * como argumento (args)

#forma optima  de sumar valores
def suma_total(numeros):
    return sum([*numeros])

resultado2 = suma_total([5,6,7,8,8,9,16])
print(resultado2)

#lo mismo que arriba utilizando el operador * como argumento (*args )
def suma(nombre,*numeros):
    return f"{nombre}, la suma de todos tus numeros es: {sum(numeros)}"

resultado = suma("Sebas",5,6,7,8,8,9,16)
print(resultado)

