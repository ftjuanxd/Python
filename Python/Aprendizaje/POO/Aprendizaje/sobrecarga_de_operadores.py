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
    
    #defino lo que hara la clases al sumar sus objetos
    def __add__(self,otro):
        nuevo_valor =self.edad + otro.edad
        return Persona(self.nombre + otro.nombre,nuevo_valor)
zone = Persona("lucas",18)
dalto = Persona("Zone",34)
maria = Persona("Maria",34)

resultado = zone + dalto + maria
print(resultado)
print(resultado.nombre)