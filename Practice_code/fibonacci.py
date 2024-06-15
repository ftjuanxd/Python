#First Opcion
def fibo(num):
    el1 = el2 =1
    sum= 0
    for i in range(3,num+1):
        sum = el1+el2
        el1 ,el2 = el2,sum
    return sum

print(fibo(9))
#Second Opcion
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)
 
print(fib())