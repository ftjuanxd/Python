fact = {}
value =0.0
opc = int(input("\tBienvenido. \n1.Anadiar factura.\n2.Pagar Factura.\n3.Salir\nOpcion:"))
while True:
	if opc == 1:
		opc = input("Codigo de Factura:")
		value =float(input("Valor de la factura"))
		fact[opc] = value
		if fact.get(opc) !=None:
			print("Factura registrada. ")
		else:
			print("Factura no registrada.")
	elif opc == 2:
		opc = input("Codigo de Factura:")
		if fact.get(opc) != None:
			print("El valor de la factura es:"+fact[opc])
			value = fact[opc]
			fact.pop(opc)
		else:
			print("Factura inexistente.")
	elif opc == 3:
		print(f"Cantidad Cobrada: {value}")
		for i in fact.keys():
			print(i)
		break
