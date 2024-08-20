import random

numbers = [1,2,3,4,5,6,7,8,9,0,12,3,4,3,3,5,5,3,2,1,7,98,87,116,16]

number_random = random.randint(0,10) 

print(f'El programa genero el sigiuente numero {number_random} y lo buscara dentro de la lista la cantidad de coincidencias es de: {numbers.count(number_random)}')
