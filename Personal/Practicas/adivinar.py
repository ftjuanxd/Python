import random

upper_limit = 100
down_limit = 0

number = random.randint(down_limit,upper_limit)

number_user =int(input("Adivine el numero: "))

if number == number_user:
	print("Adivinaste el numero, Felicidades.")
else:
	print("Fallaste, sigue intentando.")
print(f'El numero era: {number}.')
