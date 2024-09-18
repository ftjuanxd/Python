#creando funcion suma numeros
def sumar_dos():
    while True:
        #iniciando numeros
        a = input("Numero 1: ")
        b = input("Numero 2: ")
        #intentando convertir los numero a enteros
        try:
            resultado = int(a)+int(b)
        #si lanzo una excepcion, pedirl que reingrese los datos
        except Exception as e:
            print("Digite un numero no sea payaso")
            print(f"Error: {type(e).__name__}")
        #si todo salio bien terminamos el bucle
        else:
            break
        #siempre se ejecutara sin importar si se cumple la excepcion o no
        # finally:
        #     print("Esto se ejecuta siempre")
    #retornando valor
    return resultado

print(sumar_dos())