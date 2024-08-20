topic = list()
losted = list()
opc = ""
while  opc != "n":
	topic.append(input("Type your topics: "))
	opc = float(input("Type your note: "))
	if  opc <5.0:
		losted.append(topic[-1])
	opc = input("do you wish continue s/n:")
if len(losted) != 0:
	print(f"You must repeat the next topics: {losted}.")
else:
	print("You mustn't repeat none topic.")
