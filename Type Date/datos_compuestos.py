#lista conjunto de datos Se puede modificar
lista = ["Cadena","Soy dalto",True,1.67]

#tupla - NO se puede modificar
tupla = ("Cadena","Soy dalto",True,1.67)

#esto es valido
lista[3]= False

#Esto no es valido
#tupla[3]= False

#creando un conjunto (set) no nos deja modficar un datos espefico sin embargo si lo podemos reescribir completo
conjunto = {"Cadena","Soy dalto",True,1.67,1.67}

#no se puede mostrar por indice
#print(conjunto[1])

#el conjunto no almacena valores duplicados , tienen orden
print(conjunto)

#creando un diccionario // los parametros para llamar los datos son los que creamos

diccionario = {#struct key : value
    'nombre' : "Juan",
    'edad' : "27",
    'esta_wey' : False,
    'altura' : 1.67
}

#asi seria como se llama
print(diccionario['altura'])