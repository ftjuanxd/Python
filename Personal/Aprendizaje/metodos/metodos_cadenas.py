cadena1  ="Hola,soY,Zone"
cadena2  ="12345"
#nos indica que funciones pidemos utilizar con el dato que le damos a dir
resultado =  dir(cadena1)
#convierte a mayuscula
mayuscula = cadena1.upper()

#convierte a minuscula
minuscula = cadena2.lower()

#convierte primer letra en mayuscula
primera_letra = cadena1.capitalize()

#buscamos una cadena en otra cadena si no encuentra un valor nos devuelve -1 de lo contrario nos devolvera la posicion donde se encuentra
busqueda_find =  cadena1.find("Z")

#buscamos una cadena en otra cadena se trabaja de la misma manera que find solo que cuando no encuentra la letra nos da una excepcion como retorno que no nos deja continuar
busqueda_index = cadena2.index("2")

#is numerico devuelve true 
is_numeric = cadena2.isnumeric()

#si es alfa numerico  nos devuelve true sino false el espacio no es un valor alfanumerico solo lo son de la A-Z
is_alfa = cadena1.isalpha()

#contamos cantidad de coincidencias dentro de otra cadena
contar_coincidencias = cadena1.count("on")

#cuenta la cantidad de caracteres de una cadena
contar_caracteres = len(cadena1)

#verificamos si una cadena empieza con otra cadena dada, si es asi devuelve true
empieza_con = cadena1.startswith("Hola")

#verificamos si una cadena termina con otra cadena dada, si es asi devuelve true
termina_con = cadena1.endswith("Zone")

#reemplaza un pedazo de la cadena dada por otra dada, si el valor 1 se, encuentra en la cadena original, reemplaza el valor de 1 de la misma por el valor 2
cadena_nueva = cadena1.replace(","," ")

#separar cadenas con la cadena que le pasemos

cadena_separada = cadena1.split(",")

print(cadena_separada[1])
print(type(cadena_separada))