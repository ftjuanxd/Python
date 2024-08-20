#modulo de expresiones reguales comun
import re

texto = """hola maestro, como estas 1. como estas mi capitan
esta es la segunda linea de texto223 abb...
y ahora si te dejo de joder por qu3e es la final..abb
"""
#Busca el primer parametro que coincida
#resultado = re.search("joder",texto)

#Busca todos los parametros que coincidan
#resultado = re.findall("joder",texto)

# #Busca todos los parametros que coincidan ignorando mayusculas
# resultado = re.findall("joder",texto,flag=re.IGNORECASE)

#\d --busca digitos numericos del 0 al 9
#con la r le decimos al softwae que vamos a utilizar expresiones regulares
#resultado = re.findall(r"\d",texto)

#\D --busca TODO menos digitos del 0 al 9
#resultado = re.findall(r"\D",texto)

#\w -> busca caracteres alfanumericos [a-z, A-Z 0-9 y _]
#resultado = re.findall(r"\w",texto)

#\W -> busca TODO menos caracteres alfanumericos [a-z, A-Z 0-9 y _]
#resultado = re.findall(r"\W",texto)

#\s -> busca espacios en blanco -> espacios, tabs, saltos de linea
#resultado =re.findall(r"\s",texto)

#\S -> busca TODO menos espacios en blanco -> espacios, tabs, saltos de linea
#resultado =re.findall(r"\S",texto)

#. BUsca TODO menos salto de linea
#resultado =re.findall(r".",texto)

#\n Busca los saltos de linea
#resultado =re.findall(r"\n",texto)

#\-> cancela caracteres especiales, cancelando la funcion del punto y buscando puntos
#resultado = re.findall(r'\.',texto)

#aramndo una cadena que busque un numero, seguido de un punto y un espacio

#resultado = re.findall(f"\d\.\s",texto)

#^ Buscando el inicio de una linea, buscando un palabra al principio de la linea
#flags=re.M activa multilinea
#resultado = re.findall('^esta',texto, flags=re.M)

#$ buscando el final de una linea
#resultado = re.findall('capitan$',texto, flags=re.M)

#(n) -> busca n cantidad de n el valor de la izquierda
#resultado = re.findall(r'\d{3}\s',texto)

#{n,m} -> al menos n, como maximo m
resultado = re.findall(r'\d{1,4}',texto)

# | -> busca una cosa o la otra
resultado = re.findall(r'\d{1,4}|hola',texto)

#* nos busca todas o ninguno de los valores pediudo y no afecta la expresion si no encuentra
print(resultado)