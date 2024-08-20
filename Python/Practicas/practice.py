phrase = input("Digite un caracter: ")

if phrase.isnumeric() == True:
	print("Digito un numero.")
elif phrase.isalpha() == True:
	print("Digito una letra.")
else :
	print("Digito un caracter especial.")
