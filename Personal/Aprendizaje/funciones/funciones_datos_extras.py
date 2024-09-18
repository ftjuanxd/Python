#creando una funcion de 3 paramteros
# def frase (nombre,apellido,adjetivo):
#     return f"Hola {nombre} {apellido}, sos muy {adjetivo}"

# frase_resultante = frase(adjetivo="Pro",nombre="Sebastian", apellido ="Zone")
# print(frase_resultante)

#creando la misma funcion con un parametro opcion y un valor por defecto
def frase (nombre,apellido,adjetivo="pro"):#parametro por defecto adjetivo
    return f"Hola {nombre} {apellido}, sos muy {adjetivo}"

frase_resultante = frase("Sebastian","Zone","Smart")#parametro opcional adjetivo
print(frase_resultante)