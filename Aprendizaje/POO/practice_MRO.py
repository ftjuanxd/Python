class Numbers:
    def __init__(self):
        self.numbers = []
    
    def Give_Numbers(self):
        opc = ""
        while opc != "n" : 
            try:
                n1 =  int(input("Type a number: "))
                self.numbers.append(n1)
                opc = input("Do you wish to continue? S/N").lower()
            except ValueError:
                print("Please a enter a valid number. Stupid")
    
    def return_numbers(self):
        return [x for x in self.numbers]
    
class Calculadora (Numbers):
    def __init__(self,numbers):
        self.numbers = numbers        
    def menu(self,list):
        print("\b\t\tCalculator\b\n")
        #Show Options
        for pos,value in enumerate(list):
            print(f"{pos+1}.\t{value}\n")    
        #Request a Number
        return int(input("Which number do you choose?: "))
    #Methods of Calculator
    
    def operac(list,opc):
        res = list[0]
        for i in list[1:-1]:
            exp = str(i)+opc+str(res)
            res = eval(exp)
        return f'The results of operation is:{res}'
    def Even_Odd(self):
        results = []
        for number in self.numbers:
            if number == 0:
                results.append(f"{number} is Zero")
            elif number % 2 == 0 : 
                results.append(f"{number} is Even.")
            else:
                results.append(f"{number} is Odd.")
        return results
    
    def Mayor_Menor_que(self):
        return f"The largest number is: {max(self.numbers)} and the smallest number is: {min(self.numbers)}"
    
dict = {
    '+':"Plus",
    '-':"Less",
    '*':'Times',
    '/':'Division',
    '%':'Mod',
    '**':'Potencia'
}

obj_num = Numbers()
obj_num.Give_Numbers()

calc = Calculadora(obj_num.numbers)

opc = calc.menu(dict)

nums = []
if 1 <= opc <= len(list):     
    value = list[opc-1]
    method = getattr(calc,value)
    print(method())
else:
    print("Kind Of")    
    #modificar el metodo para mostrar y reccorer el diccionario y terminar de organizar los nuevos cambios