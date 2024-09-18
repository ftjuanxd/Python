number = int(input("Type a number:"))

num=list()

for i in range(number+1):
	num.append(i)
for j in num[::-1]:
	print(j)
