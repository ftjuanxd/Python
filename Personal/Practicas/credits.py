credit = {'Matematicas':6,'Fisica':4,'Quimica':5}

keys =  credit.keys()
total = 0
for i in keys:
	print(f"{i} tiene {credit[i]} creditos")
	total += credit[i]

print("El total de creditos de las materias es: ",total)
