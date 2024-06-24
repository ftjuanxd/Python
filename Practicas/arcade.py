try:
	age= int(input("Digite su Edad: "))
except ValueError:
	print("Digite solo numeros.")
else:
	money = 0
	if age < 4:
		print("Usted no paga entrada.")
	elif age >=4 and age <=18 :
		print("Debe pagar 5 USD.")
		money += 5
	else:
		print("Debe pagar 10 USD.")
		money+=10

