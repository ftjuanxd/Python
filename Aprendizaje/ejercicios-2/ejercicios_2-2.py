#creando una funcion que nos devuelva los numeros primos 
#entre 0 y el arguemento que pase el usuario
#crear una funcion que verifique si un nunmero es primo
def es_primo(num):
    #verificamos si el numero pasado no puede dividirse por ningun numero entre dos y ese mismo numero-1 
    for i in range(2,num-1):
        #si es divisible por algun numero retorna false y termina el bucle 
        if num%i==0: 
            return False
    #si termina el bcule significa que es no fue divisble entonces es primo
    return True
#creando una funcion que retorna una lista de numeros primos hasta el numero dado
def primos_hasta(num):
    #creamos la lista donde se van a guardar los numeros primos
    primos = []
    for i in range(3,num+1):
        resultado=es_primo(i)
        #utilizamos la funcion anterior en caso de ser True la guardamos en la lista 
        if resultado == True:
            primos.append(i)
    return primos

number = int(input("Digite un numero: "))

resultado = primos_hasta(number)
print(resultado)
