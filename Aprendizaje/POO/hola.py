def operac(list,opc):
    res = list[0]
    for i in list[1:-1]:
        exp = str(i)+opc+str(res)
        res = eval(exp)
    return f'The results of operation is:{res}'
num = [1,2,3,4,5,6,7,8,9,0]
opc = ['+','-','*','/']
print(operac(num,opc[1]))