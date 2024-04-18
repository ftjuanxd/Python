cant_inversion = float(input("Digite la cantidad a invertitr: "))
interes_anual = float(input("Digite el interes anual: "))
anual = int(input("Digite la cantidad de anios de la inversion: "))

for i in range(1,anual+1):
	cant_inversion = i*(cant_inversion+(cant_inversion*interes_anual))
	print(f"Durante el primer {i} anio de inversion se obtuvo un capital de: {cant_inversion}")
