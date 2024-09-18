#creando diccionario con dict()
diccioonario = dict(nombre="lucas",apellidos = "daltp")

#las listas no pueden ser claves y usamos frozenser para mete conjuntos
diccioonario={("dalto","rancion"):"jaja"}

#creando diccionario con front keys() valor de defecto none
diccioonario= dict.fromkeys(["nombre","apellido","suscriptores"])

#creando diccionario con front keys() con dos parametros

diccioonario= dict.fromkeys(["nombre","apellido"],"no se")

print(diccioonario)