import math

datos = []
opc = ""

while opc != "n":
	opc = int(input("type a number: "))
	datos.append(opc)
	opc = input("Do you wish continue s/n:").lower()

media =sum(datos)/len(datos)
print("la media de los numeros es:",media)

diferencia_2= [(x-media)**2 for x in datos ]

media_dife = sum(diferencia_2)/len(datos)

desviacion= math.sqrt(media_dife)

print("La desviacion tipica es:",desviacion)
