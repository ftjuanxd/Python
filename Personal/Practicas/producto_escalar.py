a = [1,2,3]
b = [-1,0,2]
product = int()
for a,b in zip(a,b):
	product += a*b

print(f"Producto Escalar es:{product}.")
