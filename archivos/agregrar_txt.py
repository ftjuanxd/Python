#con el atributo a agregamos
with open("archivos\\compa.txt","a",encoding="UTF-8") as archivo:
    #agregrando el archivo
    archivo.write("\nJAJAJ te gane\n")
    
        #agregando texto
    [archivo.write(f"Linea {i} agregada\n")  for i in range(1,6)]