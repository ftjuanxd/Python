numeros = [1,2,3,4,5,6,7,8,9,0]

#creando una funcion lambda para multiplicar por dos
multiplicar_por_dos = lambda x : x*2

# #creando una funcion que diga si es par o no
# def es_par(num):
#     if(num%2==1):
#         return True

# #usando filtrar con una funcion comun
# numeros_pares= filter(es_par,numeros)

#creando lo mismo con lambda
#struc lambda: lambda name_function: code
numeros_pares = filter(lambda numero:numero%2 == 0, numeros)

print(list(numeros_pares))