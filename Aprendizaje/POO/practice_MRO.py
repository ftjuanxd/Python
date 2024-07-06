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
    def Plus(self):
        plus = sum([x for x in self.numbers])
        return f"The results plus of numbers is: {plus}"
        
    def Less(self):
        less -=[i for i in self.numbers]
        return f"The results less of numbers is: {less}"
    
    def Times(self):
        times *= [x for x in self.numbers]
        return f"The results times of numbers is: {times}"
    
    def Division(self):             
        divi /= [x for x in self.numbers]
        if 0 in self.numbers:
            return "No se puede dividir por cero."
        return f"The results division of numbers is {divi}"
    
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
    
list = ["Plus","Less","Times","Division","Even_Odd","Mayor_Menor_que"]

obj_num = Numbers()
obj_num.Give_Numbers()

calc = Calculadora(obj_num.numbers)

opc = calc.menu(list)

nums = []
if 1 <= opc <= len(list):     
    value = list[opc-1]
    method = getattr(calc,value)
    print(method())
else:
    print("Kind Of")    