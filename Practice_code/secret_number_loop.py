secret_number = 777

print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")
number = int(input('type a number: '))

while number != secret_number:
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    number = int(input('type a number: '))
print("¡Bien hecho, muggle! Eres libre ahora.")