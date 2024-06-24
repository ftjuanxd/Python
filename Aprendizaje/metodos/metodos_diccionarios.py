diccionario = {
    "nombre" : "Sebas",
    "apellido":"Rodriguez",
    "subs" : 1000000
}
#devuelve las claves del dicionarios/ tambien nos sirve para iterar
claves= diccionario.keys()

#obteniendo un elemento con get sino lo encuentra nos devuelve none sin embargo nos deja continuar el programa
valor_de_datos= diccionario.get("nombre")

#eliminando todo del diccionario
#diccionario.clear()

#eliminando un elemento del diccionario
diccionario.pop("apellido")

#obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()

print(diccionario_iterable)