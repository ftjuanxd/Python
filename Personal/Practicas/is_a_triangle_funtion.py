def is_a_triangle(a, b, c):
    if a + b <= c or b + c <= a or c + a <= b:
        return False
    return True

def Pitagoras(a,b,c):
    if not is_a_triangle(a,b,c):
        return False
    if c > a and c > b: 
        return c**2 == a**2 + b**2 
    if a > c and a > b:
        return c**2 == a**2 + b**2

c1 = float(input("Type the value of side 1: ")) 
c2 = float(input("Type the value of side 2: "))
c3 = float(input("Type the value of side 3: "))

print(f"El resultado en base a estos numero es: {Pitagoras(c1,c2,c3)}")
