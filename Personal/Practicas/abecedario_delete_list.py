abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","x","y","z"]
for i in range(len(abc),1,-1):
	if  i%3 == 0:
		abc.pop(i-1)
print(abc)
