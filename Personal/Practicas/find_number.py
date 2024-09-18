#First Option
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False

for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break

if found:
    print("Elemento encontrado en el índice", i)
else:
    print("ausente")

#Second Option
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = int(input("Type the number what wish do you search: "))
try:
    n=my_list.index(n)
    print(f"The number have been Found and its position is {n+1}.")
except ValueError:
    print("Number not found")

