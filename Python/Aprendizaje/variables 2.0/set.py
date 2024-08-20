#creando un conjunto con la funcion set()

conjunto = set(["dato 1", ("datosenlistas1","datosenlista2")])

#metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset({"dato 1","dato 2"})#frozenset congela los parametros y nos permite colocarlos dentro de otro conjunto
conjunto2 = {conjunto1, "dato2"}

print(conjunto2)

#teoria de conjuntos

conjunto1 = {1,2,3,4}
conjunto2 = {1,4,3}

#issubset examina los datos que se le pasan para saber si el primer dato es subconjunto del segundo
resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1

#verificando si es un superconjunto
resultado = conjunto1.issuperset(conjunto2)
resultado = conjunto1 > conjunto2

#verificando si hay algun numero en comun el resultado sera true cuando no tiene ningun dato en comun
resultado = conjunto1.isdisjoint(conjunto2)

print(resultado)