#clase la receta para crear un objeto
#sneik_case 
#camelCase (todas las primeras letras van en mayusculas sin espacios, excepto la primera)
#PascalCase(todas las primeras letras van en mayusculas sin espacios), se usa para definir clases
class Celular:
    #Constructor esto se ejecuta automaticamente
    def __init__(self,marca,modelo,camara):
        self.marca = marca
        self.modelo = modelo 
        self.camara = camara

    def llamar(self):
        print(f"Estas haciendo un llamado desde un {self.modelo}")
    
    def cortar(self):
        print(f"Cortaste la llamada desde un {self.modelo}")
    
celular1 = Celular("Apple","IPhone 15","48MP")
celular2 = Celular("Samsung","S24","100MP")

celular1.llamar()
celular2.cortar()