#abriendo el archivo con with open
with open("archivos\\compa.txt",encoding="UTF-8") as archivo:
    
    #leemos el archivo
    contenido =archivo.read()
    
    #mostrando el archivo
    print(contenido)

#no es necesario cerrarlo con with open