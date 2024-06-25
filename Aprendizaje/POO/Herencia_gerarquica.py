class Persona:
    def __init__(self, nombre, edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    
    def hablar(self):
        print("Hola estoy hablando un poco")
    
class Empleado(Persona):
    #para agregar mas parametros debemos usar super
    def __init__(self,nombre,edad,nacionalidad,trabajo,salario):
        super().__init__(nombre,edad,nacionalidad)
        self.trabajo = trabajo
        self.salario = salario
        
class Estudiante(Persona):
    #para agregar mas parametros debemos usar super
    def __init__(self,nombre,edad,nacionalidad,notas,instituto):
        super().__init__(nombre,edad,nacionalidad)
        self.notas = notas
        self.instituto = instituto
        
roberto =  Empleado("roberto",34,"argentino","Programador","$10000")

Juan = Estudiante("Juan",23,"colombia",3.8,"Julio Florez")


roberto.hablar()