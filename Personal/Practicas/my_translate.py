translate = {}
trans = list()
number = int(input("How many words do you wanna add?: "))
for i in range(number):
	phrase = input("Type a phrase and your Traduction: ").lower()
	spanish,english = phrase.split(":")

	translate[spanish]=english
else:
	phrase = input("Type your Phrase: ")
	phrase = phrase.split(" ")
	for i in  phrase:
		if translate.get(i)!= None:
			trans.append(translate[i])
		else:
			trans.append(i)
	else:
		for i in trans:
			print(i,end=' ')
print("\nBye")
