numeros = [3,4,5,6,7,8]

#encontrando el numero maximo y menor de una lista /solo numeros
numero_max_alto = max(numeros)
print(numero_max_alto)

#encontrando el numero menor de una lista / solo numeros
numero_max_menor = min(numeros)
print(numero_max_menor)

#redondeando a 2 decimales / solo numeros
numero = round(16.9456,2)
print(numero)

#retorna false -> 0, vacio, False, ninguno \ True -> distinto de cero, cadena de texto, datos no vacios
resultado_bool = bool([])

#retorna true, si todos los valores son verdaderos
resultado_all = all([123,"juan",[343,5]])

#suma todos los numeros dentro de un iterables / solo numeros
sum_total = sum(numeros)

print(sum_total)