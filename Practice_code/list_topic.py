opc = ""
lista = list()
while opc != "n":
	opc = input("Type a topic:")
	lista.append(opc)
	opc = input("You wish contiinue s/n:").lower()
print(f"The list of topic it's: {lista}")
