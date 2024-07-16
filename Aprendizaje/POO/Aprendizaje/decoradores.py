#un decorador es una funcion que agrega codigo a una funcion ya existente
def decorador(funcion):
    def funcion_modificada():
        print("Antes de llamar la funcion.")
        funcion()
        print("Despues de llamar la funcion.")
    return funcion_modificada
#forma base de usar un decorador
# def saludo():
#     print("hola salto")
    
# #declarandon la variable del decorador 
# saludo_ = decorador(saludo)

# saludo_()

#forma optima
@decorador
def saludo():
    print("Hola pende")
    
saludo()