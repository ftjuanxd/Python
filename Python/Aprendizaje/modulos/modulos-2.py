#si el modulo estuviera dentro de una carpeta en la misma ruta
#import funciones_buenas.saludar as fb

import sys

#modulos por fuera de la carpeta
sys.path.append("c:\\Users\\miyam\\desktop\\Python\\funciones_buenas")

import saludar as md


print(md.saludar("Zone"))

#con esto podemos los modulo propios de python
#print(sys.builtin_module_names)

#con esto vemos la ruta de los modulos
#print(sys.path)
#print(fb.saludar("Zone"))