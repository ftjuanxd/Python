#abriendo archivo con codificacion UTF-8(universal)
archivo_sin_leer = open("archivos\\compa.txt",encoding="UTF-8")
#Leyendo archivo completo- solo una vez desde el open
#archivo = archivo_sin_leer.read()

#leer linea por linea
#lineas = archivo_sin_leer.readlines()

#leer una sola linea sino lee una linea completa lee hasta la cantidad de caracteres
linea = archivo_sin_leer.readline(20)

#cerrar el archivo
archivo_sin_leer.close()

print(linea)
