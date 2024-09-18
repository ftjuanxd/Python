#son palabras reveservadas que empiezan con dos guiones bajos y terminan con dos guiones bajo
class Persona:
    
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    #Crear metodo para imprimirse en pantalla en modo de texto
    def __str__(self):
        return f"Persona(nombre={self.nombre},edad={self.edad})"
    
    def __repr__(self):
        return f'Persona("{self.nombre}",{self.edad})' 
    
zone = Persona("lucas",18)

print(zone)

repre = repr(zone)
print(repre)
rest = eval(repre)

print(rest)