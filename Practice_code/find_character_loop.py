phrase = input("Type a phrase: ")
char =  input("Type a character: ")
count = 0
for i  in phrase.lower():
	if i == char:
		count +=1

print(f"The count of once that is *{char}* in *{phrase}* it's: {count}")
