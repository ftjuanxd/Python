import math

numbers = list()
media = 0
opc = ""
diferent=0

while opc != "n":
	opc = int(input("Type a number:"))
	numbers.append(opc)
	opc = input("Do you wishing continue s/n: ").lower()

for i in numbers:
	media += i
media /= len(numbers)
print(f"La media de los numeros es:{media}")
for n in numbers:
	diferent +=pow((n-media),2)
diferent /= len(numbers)
diferent = math.sqrt(diferent)
print(f"La desviaccion tipica del conjunto de numeros: {numbers} es: {diferent}.")
