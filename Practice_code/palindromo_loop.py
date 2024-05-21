word = input("type a word: ")

for w,i in zip(word, word[::-1]):
	if w!=i:
		print("No es palindroma")
		break
else:
	print("La palabra es palindroma")
