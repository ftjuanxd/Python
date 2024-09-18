def fibonacci_hasta(num):
    a,b=0,1
    fibonacci= [0]
    for i in range(num):
        if b > num: return fibonacci
        else: 
            fibonacci.append(b)
            a,b = b,a+b
            
number = int(input("Digite un numero: "))

resultado = fibonacci_hasta(number)

print(resultado)