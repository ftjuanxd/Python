class Estudiante:
    def __init__(self, nombre, edad,grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        
    def estudiar(self):
        print("Estudiando....")
    
    def mostrar_estudiante(self):
        print(f"""DATOS DEL ESTUDIANTE: \n\n
                Nombre: {estudiante.nombre}\n
                Edad: {estudiante.edad} \n
                Grado: {estudiante.grado} \n
            """)
        
while True:
    try:    
        nombre = input("Type your name: ")
        edad = int(input("Type your age: "))
        grado = input("Type your grade: ")
        break
    except ValueError:
        print("La edad es un numero el resto texto")

estudiante = Estudiante(nombre,edad,grado)

estudiante.mostrar_estudiante()

while True:
    estudiar = input()
    if (estudiar.lower() == "estudiar"):
        estudiante.estudiar()
        break