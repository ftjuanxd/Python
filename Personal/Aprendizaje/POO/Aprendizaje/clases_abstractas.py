#plantilla para crear clase apartir de esta
from abc import ABC ,abstractclassmethod#decorador que permite decir que una clase es abstracta
#plantilla de persona 
class Persona(ABC):
    
    @abstractclassmethod
    def __init__(self,nombre,edad,sexo,actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
    
    @abstractclassmethod
    def hacer_actividad(self):
        pass
    
    def presentarse(self):
        print(f"Hola, me llamo: {self.nombre} y tengo {self.edad} anios.")
        

class Estudiante(Persona):
    
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)    
    
    def hacer_actividad(self):
        print(f"Estoy estudiando :{self.actividad}")

class Trabajador(Persona):
    
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)    
    
    def hacer_actividad(self):
        print(f"Actualmente estoy trabajando en el rubro de:{self.actividad}")

zone = Estudiante("Zone",18,"Masculino","Programacion")

nastic = Trabajador("Nastic",19,"Femenino","Enfermeria")

zone.presentarse()

zone.hacer_actividad()

nastic.presentarse()

nastic.hacer_actividad()