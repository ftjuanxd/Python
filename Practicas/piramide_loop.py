blocks = int(input("Type a number blocks: "))
blocks_need = 1
height = 0
while blocks >= blocks_need:
    blocks -= blocks_need
    height += 1
    blocks_need +=1
    
print("La altura maxima conseguida es: ",height)