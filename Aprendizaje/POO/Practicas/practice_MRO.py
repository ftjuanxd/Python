class Numbers:
    def __init__(self):
        self.numbers = []
    
    def Give_Numbers(self):
        opc = ""
        while opc != "n" or len(self.numbers) < 2 : 
            try:
                n1 = int(input("Type a number: "))
                self.numbers.append(n1)
                opc = input("Do you wish to continue? S/N: ").lower()
                if opc == "n" and len(self.numbers) < 2:
                    print("You need to enter at least two numbers.")
                    opc = ""
            except ValueError:
                print("Please a enter a valid number. Stupid")
    def return_numbers(self):
        return [x for x in self.numbers]
    
class Calculadora (Numbers):
    def __init__(self,numbers):
        self.numbers = numbers        
    def menu(self,dic):
        print("\b\t\tCalculator\b\n")
        #Show Options
        for pos,value in dic.items():
            print(f"{pos}.\t{value}\n")    
        #Request a Number
        return input("Which symbol do you choose?: ")
    #Methods of Calculator
    
    def operac(self,opc):
        res = self.numbers[0]
        for i in self.numbers[1:]:
            try:
                exp = str(i)+opc+str(res)
                res = eval(exp)
            except ZeroDivisionError:
                return "Error in the process. Division by zero."
            except Exception:
                return("Error in the process. Review the numbers. Warning with the Zero.")
        return f'The results of operation is:{res}'
    
dic = {
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

opc = calc.menu(dic)
value = dic.get(opc)

if value != None:
    for i in dic.items():
        if opc in i:
            print(calc.operac(opc))
            break
else:
    print("Kind Of")    