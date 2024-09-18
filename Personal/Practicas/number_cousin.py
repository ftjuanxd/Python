number = int(input("Type a number: "))
co = True
for i in range(2,100,number):
	if number%i == 0:
		print("It's not Cousin Number")
		co = False
		break
if co != False:
	print("It's Cousin Number")
