number = list()
opc =""
while opc != "n":
	opc =int(input("type a number lotery:"))
	number.append(opc)
	opc = input("do you wish continue s/n: ")
number.sort()
print(f"The numbers winner they're: {number}")
