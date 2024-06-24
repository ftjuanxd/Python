name = input("Type your name: ")
edad = int(input("Type your age: "))
dir = input("type your direction: ")
tel = int(input("Type your number: "))

data = dict(nombre=name,edad=edad,direccion=dir,telefono=tel)
data_i = data.keys()

print(f"{data['nombre']} tiene {data['edad']} vive en {data['direccion']} y su numero de telefono es {data['telefono']}")
