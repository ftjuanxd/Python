hat_list = [1, 2, 3, 4, 5]  # Esta es una lista existente de números ocultos en el sombrero.

number = int(input("Type a number: "))

hat_list.insert(2,number)

hat_list.pop(3)

print(len(hat_list))

print(hat_list)

