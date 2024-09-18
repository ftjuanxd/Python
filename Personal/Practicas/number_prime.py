def is_prime(num):
    for i in range(2,num-1):
        if num % i == 0:
            return False
    else:
        return True
        
number = int(input("Digite un numero: "))
if is_prime(number):
    print("The number is prime.")
else:
    print("The number isn't prime")