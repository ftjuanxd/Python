#Acceder a propiedades y metodos privados e incluso modificarlo
class Persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self.__edad =edad
    #obtener valores privados y super privados dentro de la misma clase
    #getters
    def get_nombre(self):
        return self.__nombre
    #definir un valor a un atributo de la clase o reescribir un valor
    def set_nombre(self,new_nombre):
        self.__nombre = new_nombre

    #Tambien se puede un solo getter and setter con la siguiente estrucutura - DRY
    #solo cambiar el numero de guion bajos dependiendo del nivel de las variables 
    def set_attribute(self,attribute,value):
        self.__attribute = value
        
    def get_attribute(self,attribute):
        return self.__attribute
#instanciando la clase
zone = Persona("Sebastian",18)

#obtener el valor de la clase
nombre = zone.get_nombre()

#mostrar nombre
print(nombre)

#Reescribir el valor de nombre
zone.set_nombre("Zonenastic") 

#obtener el nuevo valor de nombre   
nombre = zone.get_nombre()

#imprimir
print(nombre)

zone.set_attribute("nombre","n")    

print(zone.get_attribute("nombre"))
