people = {}
opc = ''
keys = ["Name","Age","Gender","Phone","Email"]
while opc != 'n':
	for i in keys:
		people[i] = input(f"Type your {i}:")
		print(people)
	opc = input("Do you wish continue: s/n").lower()
