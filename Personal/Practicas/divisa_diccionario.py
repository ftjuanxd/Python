divisa = { "Euro":"E", "Dollar":"$","Yen":"Y"
}
_opc = input("Type your divisa: ").title()

if divisa.get(_opc) != None:
	for div in divisa.items():
		key = div[0]
		value = div[1]

		if key == _opc:
			print(key,":",value)
else:
	print("La divisa no existe.")
