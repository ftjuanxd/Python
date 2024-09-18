#pedir la edad de los compañeros que vinieron hoy a clase y ordena los datos de menro a mayor
#el mayor es el profesor y el menor es el asistente ¿ quien es quien?
#funcion para obtener el asistente y al profesor segun la edad
def obtener_companeros(cantidad):
    
    #creando la lista con compañeros
    compañeros = []
    
    #ejecutando un for para pedir informacion de cada compañero
    for i in range(cantidad):
        nombre = input("ingrese la nombre del compañero: ")
        edad = int(input("ingrese la edad el compañero: "))
        compañero = (nombre,edad)
        
        #agregando la informacion a la lista
        compañeros.append(compañero)
    
    #ordenandolos de menor a mayor segun su edad
    compañeros.sort(key=lambda x:x[1])
    
    #compañeros[x] devuelve una tupla con (nombre,edad) y despues accedemos al nombre para definir al asistente y el profesor
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    
    #retornamos una tupla
    return asistente,profesor


cantidad_de_estudiantes = int(input("Digite la cantidad de estudiantes: "))

#desempaquetamos lo que nos retorna la funcion
asistente,profesor = obtener_companeros(cantidad_de_estudiantes)

#mostrando el resultado
print(f"El profesor es: {profesor} y su asistente es {asistente}")

