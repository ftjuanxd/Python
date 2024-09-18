topic = list()
note = list()
opc = ""
while opc != "n":
	opc = input("Type a topic: ")
	topic.append(opc)
	opc = int(input("Type the note correspond at topic:"))
	note.append(opc)
	opc = input("you wishing continue s/n:").lower()
for t,n in zip(topic,note):
	print(f"In {t} has got {n}")
