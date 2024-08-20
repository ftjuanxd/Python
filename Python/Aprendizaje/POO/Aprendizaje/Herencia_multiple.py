class Persona:
    def __init__(self, nombre, edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    
    def hablar(self):
        print("Hola estoy hablando un poco")
    
class Artista:
    def __init__(self,habilidad):
        self.habilidad = habilidad
        
    def mostrar_habilidad(self):
        return f"Mi habilidad es: {self.habilidad} "
    
class EmpleadoArtista(Persona,Artista):
    
    def __init__(self, nombre, edad,nacionalidad,habilidad,salario,empresa):
        Persona.__init__(self,nombre, edad,nacionalidad)
        Artista.__init__(self,habilidad)
        self.salario = salario 
        self.empresa = empresa
    
    def presentarse(self):
        #return f'{self.mostrar_habilidad()}' #llamdo a funcion heredada     
        print(f" Hola soy {self.nombre}, {self.mostrar_habilidad()} y trabajo en {self.empresa}")#llama a la funcion desde la clase padre sin dejar posibles modificaciones dentro de la clase hija
roberto =  EmpleadoArtista("roberto",34,"argentino","Arte Moderno","$10000","Photoshop")

#roberto.presentarse()

herencia =  issubclass(Persona,Artista)#nos indica si una clase hereda de la otra  (clase1, clase heredad) siempre retornara un valor booleano

instancia = isinstance(roberto,Artista) #me permite ver si este objeto es de X clase (objeto,clase) y retorna un valor booleano esto tambien aplicarea si un objeto de una clase hija se compara con la clase padre de esta (objeto_clase_hija, clase padre)
print(instancia)
print(herencia)