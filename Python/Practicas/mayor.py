#Mayor numero con bucles e if
# number = []

# for i in range(3):
#       number.append(int(input("Type a number: ")))
# else:
#     n = number[0]
#     for i in number:
#         if i > n:
#             n = i
#     else:
#         print('El numero vencedor es:',n)

#mayor numero con bucles e max

number = []

for i in range(3):
      number.append(int(input("Type a number: ")))
else:
    print('El numero vencedor es:', max(number) )