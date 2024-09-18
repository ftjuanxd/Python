data ={}
opc=""
value=""
#while opc != "n":
while True:
	try:
		opc=input("Type a Frute: ")
		value =float(input("Type the value:"))
	except ValueError as a :
		print('Intentalo otra vez')
		print(f'Error: {type(a).__name__}')
	else:
		data[opc]=value
#		opc = input("Do you wish continue:")
		break
opc = input("Type a Frute to search:").lower()
for clave,valor in data.items():
	if opc == clave:
		weight = float(input("Type the weight: "))
		print(f"Esta cantidad de kilos de {clave } vale: {valor*weight}")
		break
else:
	print(f"La fruta {opc} no existe.")
