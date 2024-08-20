class Estudiante:
    def __init__(self, nombre, edad,grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        
pedro = Estudiante("Pedro","23","1")

print(pedro.nombre)