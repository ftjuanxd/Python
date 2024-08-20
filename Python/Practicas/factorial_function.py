# def fact (num):
#     fact = 1
#     for i in range(1,num+1):
#         fact *= i
#     return fact


# for i in range(1,16+1):
#     print(i,fact(i))
    
def fact_re (num):
    if num < 0:
        return None
    if num < 2:
        return 1
    return num* fact_re(num-1)

print(fact_re(6))