tablero = [[],[],[],[],[],[],[],[]]

for i in enumerate(tablero):
	indice_i = i[0]
	content = i[1]
	for j in enumerate(content):
		indice_j = j[0]
		print(indice_i,indice_j)
