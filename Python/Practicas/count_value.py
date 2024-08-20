values = [50,75,46,22,80,65,8]
max= 0
min =1000
for i in values:
	if i > max:
		max = i
	if i < min:
		min = i

print(f"El mayor numero es:{max}, El minimo numero es:{min}.")
