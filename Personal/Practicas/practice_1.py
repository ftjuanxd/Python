#variable de control
opc = ""
contador = 0
#lista de numeros
numbers = list()

while opc != 'n' and opc != 'N':
	number = int(input("Digite un numero: "))
	numbers.append(number)
	contador += 1
	opc = input("Desea continuar S/N:")

numbers.reverse()

for i in numbers:
	print(f"El numero es: {i} y su posicion es: {contador}")
	contador -= 1
