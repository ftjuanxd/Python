class MiClase:
    def __init__(self):
        #Atributo privado
        #python compre el guion bajo inicial como un valor privado sin embargo si es posible acceder a este
        self._atributo_privado = "Valor"
        #Atributo SuperPrivado - Este si realiza un cambio sobre python
        self.__atributo = "Valor"
    
    #el atributo super privado comun mente se muestra o trabaja en metodos    
    def muestra(self):
        return self.__atributo
    #tambien existe los metodos privados y super privados
    def __hablar(self):
        return "Hola"
    
    def _hablar(self):
        return "Hola"
        
obj = MiClase()

print(obj.muestra())