my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
n = []
for i in range(len(my_list)):
    if i == 0 or my_list[i] not in n:
        n.append(my_list[i])
    
print("La lista con elementos únicos:")
print(n)

