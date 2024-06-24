try:
	type = (input("Desea Pizza Vegetariana: (S/N)")).lower()

except type!='s' or type != 'n':
	print("Solo diganos si o no.")

else:
	ingrediente = ["Mozarella","Tomate"]
	if type =='s':
		print("Los ingredientes del menu Vegetariano es:")
		print("Pimiento (P), Tofu (T).")
		type =  input("Digite la inicial del ingrediente: ").upper()

		if type == "P":
			ingrediente.append("Pimiento")
		elif type == "T":
			ingrediente.append("Tofu")
		else:
			print("El ingrediente seleccionado no existe")
		type = "Vegetariana"
	else:
		print("Los ingredientes del menu son: ")
		print("Peperoni (P), Jamon(J), Salmon (S)")
		type=input("Digite la Inicial del Ingrediente: ").upper()
		if type == "P":
			ingrediente.append("Peperoni")
		elif type == "J":
			ingrediente.append("Jamon")
		elif type == "S":
			ingrediente.append("Salmon")
		else:
			print("El ingrediente seleccionado no existe")
		type = "No Vegetariana"
	if len(ingrediente) == 3:
		print(f"La pizza es {type} y sus ingredientes son:{ingrediente} ")
	else:
		print("Error con los ingredientes")
