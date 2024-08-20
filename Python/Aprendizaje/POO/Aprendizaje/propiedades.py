#Acceder a propiedades y metodos privados e incluso modificarlo
class Persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self.__edad =edad

    @property #esto define un getter lo que permite tratarlo como una propiedad
    def nombre(self):
        return self.__nombre

    @nombre.setter #esto me permite modificar la propiedad trabajando la con el mismo nombre 
    def nombre(self,new_nombre):
        self.__nombre = new_nombre

    @nombre.deleter
    def nombre(self):
        del self.__nombre
        
tata = Persona("Manji",78)

nombre = tata.nombre
print(nombre)

tata.nombre = "Tata"

nombre = tata.nombre
print(nombre)

#esto elimina la propiedad
# del tata.nombre
try:
    nombre = tata.nombre
    print(nombre)
except Exception as e:
    print(type(e),e)