phrase = input("type a phrase: ")
vocals = ["a","e","i","o","u"]
counter = 0

for p in phrase:
	for v in vocals:
		if p == v:
			counter +=1

print(f"La cantidad de vocales dentro de la palabra es: {counter}")
