buys = {}
opc = ""
values = float()
while opc != "n":
	opc = input("Name article: ")
	values = float(input("Value Article: "))
	buys[opc] = values

	opc = input("Do you wish continue s/n: ").lower()

keys = buys.items()
print("Lista de Compras")
values = 0

for i in keys:
	print(f"{i[0]}    {i[1]}")
	values += i[1]
else:
	print(f"Total   {values}")
