#2 listas con nombre y apellido escribir los datos de forma optima en una archivo con un for

nombres = ["Lucas","Matias","Camila","Pedro"]
apellidos = ["Dalto","Romina","Parra" ]

#registrar en un txt de forma optima
with open("resolviendo_problemas\\lista_de_nombre_y_apellidos.txt","w") as arch:
    arch.writelines("Los datos son:\n")
    [arch.writelines(f"Nombre: {n}\nApellido:{a}\n-----------\n") for n,a in zip(nombres,apellidos)]