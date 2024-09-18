phrase = input("Type a phrase:").upper()
vocals = ('A',"E",'I',"O",'U')
opc = bool()
# for i in phrase:
#     if i == "A" or i == "E" or i =="I" or i == "O" or i == 'I' or i == "U":
#         continue
#     print(i)

for j in phrase:
    if j in vocals:
        continue
    print(j)