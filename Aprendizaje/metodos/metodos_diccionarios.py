diccionario = {
    "nombre" : "Sebas",
    "apellido":"Rodriguez",
    "subs" : 1000000
}
#devuelve las claves del dicionarios/ tambien nos sirve para iterar
claves= diccionario.keys()
#ejemplo de prueba
# for i in claves:
#     print(diccionario[i])

#obteniendo un elemento con get sino lo encuentra nos devuelve none sin embargo nos deja continuar el programa
valor_de_datos = diccionario.get("nombre")
print(valor_de_datos)

#eliminando todo del diccionario
#diccionario.clear()

#eliminando un elemento del diccionario
diccionario.pop("apellido")

#obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()
#ejemplo de prueba
# for key,value  in diccionario_iterable:
#     print(key,value)
print(diccionario_iterable)