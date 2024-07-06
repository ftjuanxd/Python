class Numbers:
    def __init__(self):
        self.numbers = []
    
    def give_numbers(self):
        while len(self.numbers) < 2:
            try:
                n = int(input("Type a number: "))
                self.numbers.append(n)
            except ValueError:
                print("Please enter a valid number.")

class Calculadora:
    def __init__(self, numbers):
        self.numbers = numbers
    
    def menu(self, options):
        print("\n\t\tCalculator\n")
        for pos, value in enumerate(options):
            print(f"{pos + 1}.\t{value}")    
        return int(input("Which number do you choose?: "))
    
    def Plus(self):
        return f"The result of addition is: {self.numbers[0] + self.numbers[1]}"
    
    def Less(self):
        return f"The result of subtraction is: {self.numbers[0] - self.numbers[1]}"
    
    def Times(self):
        return f"The result of multiplication is: {self.numbers[0] * self.numbers[1]}"
    
    def Division(self):
        if self.numbers[1] == 0:
            return "Cannot divide by zero."
        return f"The result of division is: {self.numbers[0] / self.numbers[1]}"
    
    def Par_Impar(self):
        results = []
        for number in self.numbers:
            if number == 0:
                results.append('0 is Zero.')
            elif number % 2 == 0:
                results.append(f'{number} is Even.')
            else:
                results.append(f'{number} is Odd.')
        return results
    
    def Mayor_Menor_que(self):
        return f"The largest number is: {max(self.numbers)} and the smallest number is: {min(self.numbers)}."

# Lista de opciones de métodos
options = ["Plus", "Less", "Times", "Division"]

# Crear una instancia de la clase Numbers y pedir los números
num_obj = Numbers()
num_obj.give_numbers()

# Crear una instancia de la clase Calculadora con los números obtenidos
calc = Calculadora(num_obj.numbers)

# Mostrar el menú y obtener la opción del usuario
opc = calc.menu(options)

# Verificar que la opción sea válida y llamar al método correspondiente
if 1 <= opc <= len(options):
    method_name = options[opc - 1]
    method = getattr(calc, method_name)
    print(method())
else:
    print("Invalid option")
