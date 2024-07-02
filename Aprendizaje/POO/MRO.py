#metodo de resolucion de orden
class A:
    def hablar(self):
        print("Hola desde A")        
class B():
    def hablar(self):
        print("Hola desde B")
class C(A,B):
    def hablar(self):
        print("Hola desde C")
        
class Short(A,B):
    pass
        
class D(C):
    def hablar(self):
        print("Hi from D.")

class J(D):
    def hablar(self):
        print("Hi from J")
        
class X(J,Short ):
    pass
        
d = J()
#d.hablar()

print(X.mro()) #muestra el orden de funcion de las clases