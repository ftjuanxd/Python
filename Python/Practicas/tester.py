# dictionary = {}
# my_list = ['a', 'b', 'c', 'd']

# for i in range(len(my_list) - 1):
#     dictionary[my_list[i]] = (my_list[i], )

# for i in sorted(dictionary.keys()):
#     k = dictionary[i]
#     print(k[0])
# k = None
# print(k)

# def fun(x):
#     if x % 2 == 0:
#         return 1
#     else:
#         return


# print(fun(fun(2)) + 1)


# def fun(x):
#     global y
#     y = x * x
#     return y


# fun(2)
# print(y)

# def any():
#     print(var + 1, end='')


# var = 1
# any()
# print(var)

# my_list =  ['Mary', 'had', 'a', 'little', 'lamb']


# def my_list(my_list):
#     del my_list[3]
#     my_list[3] = 'ram'


# print(my_list(my_list))

# dictionary = {'one': 'two', 'three': 'one', 'two': 'three'}
# v = dictionary['one']

# for k in range(len(dictionary)):
#     v = dictionary[v]

# print(v)

# tup = (1, 2, 4, 8)
# tup = tup[1:-1]
# tup = tup[0]
# print(tup)


try:
    value = input("Ingresa un valor: ")
    print(value/value)
except ValueError:
    print("Entrada incorrecta...")
except ZeroDivisionError:
    print("Entrada errónea...")
except TypeError:
    print("Entrada muy errónea...")
except:
    print("¡Buuu!")
