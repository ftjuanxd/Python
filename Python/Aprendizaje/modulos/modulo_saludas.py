#Llamamos una funcion dentro del metodo para solo usar esa
from modulos.funciones_buenas.saludar import create_password as password
import random
#llamamos todo el modulo y tenemos acceso a todas las funciones dentro de este
#import modulo_saludar as md
#uno tambien puede importar variables por tanto tener cuidado con las funciones iguales 
number = random.randint(0,9)

password(number)

#para ver las propiedades y metodos de namespace
#print(dir(modulo_random))

#accedemos el nombre del modulo llamado
print(__name__)

#accedemos al nombre del modullo llamado
#print(modulo_saludar.__name__)