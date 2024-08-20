number = int(input("Type a number: "))

impar = list()

for i in range(number+1):
	if i%2!=0:
		impar.append(i)
print(impar)
