# #creando una funcion simple
# def saludar():
#     print("Hola zone mi maestro")
# #ejecuntando una funcion simple
# for num in range(10):
#     saludar()
#creando una funcion con parametros
# def saludar(nombre,sexo):
#     sexo = sexo.lower()
#     if(sexo == "mujer"):
#         adjetivo ="Reina"
#     elif(sexo == "hombre"):
#         adjetivo = "Maestro"
#     else:
#         adjetivo = "crack"
        
        
#     print(f"Hola,{nombre} mi {adjetivo}")

# user = input("Cual es tu nombre: ")
# genero = input("Cual es tu genero: ")
# saludar(user,genero)

#crear una funcion que me retorne multiples valores valores
import random

def crear_contraseña_random(num):
    chars = "abcdefghijklmnopqrstuvxwyz."
    num_entero = str(num)#convertir un numero a entero
    num = int(num_entero[0])#para quedarnos con el primer dato digitado
    c1 = num-random.randint(0,num)
    c2 = num-random.randint(0,num)
    c3 = num-random.randint(0,num)
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return (contraseña,num)

#creando un numero aleatorio para la funcion
number_random = random.randint(0,90000)

#desempaquetando los valores de la funcion
password,primer_numero= crear_contraseña_random(number_random)

#mostrando los resultados obtenidos y los datos utilizados para obtenerla
frase = f"TU nueva contraseña es {password}"
print(frase)
print(f"El numero utilizado para crearla: {primer_numero}")

