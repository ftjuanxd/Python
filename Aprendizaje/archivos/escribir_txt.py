#con el atributo w sobreescribimos
with open("archivos\\compa.txt","w",encoding="UTF-8") as archivo:
    #sobrescribiendo el archivo
    #archivo.write("JAJAJ te gane")
    
    #agregando 2 lineas con writes lines
    archivo.writelines(["Hola maestro\n","Misericordia"])
    
    #agregando 2 lineas con writes lines
    archivo.writelines(["Buenas_copa\n"," no"])