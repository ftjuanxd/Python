opc = ""
lista =list()

while opc != "n":
	opc = input("Type a topic: ")
	lista.append(opc)
	opc = input("you wishing continue s/n:").lower()

for i in lista:
	print(f"I study {i}.")
