import random

def saludar(name):
    print(f"!hola {name}¡ Espero que hayas tenido un maravilloso dia")
    
def number_random(list):
    if (len(list) == 0):
        return random.randint(0,900000)
    else:
        return random.randint(0,len(list))

def create_password(num):
    chars = "abcdefghijklmnopqrstuvxwyz."
    num_entero = str(num)#convertir un numero a entero
    num = int(num_entero[0])#para quedarnos con el primer dato digitado
    c1 = num-number_random(chars)
    c2 = num-number_random(chars)
    c3 = num-number_random(chars)
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    print(f"TU nueva contraseña es {contraseña}")

print(__name__)