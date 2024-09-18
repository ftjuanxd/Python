# def ft_and_inch_to_m(ft, inch = 0.0):
#     return ft * 0.3048 + inch * 0.0254


# def lb_to_kg(lb):
#     return lb * 0.4535923


# def bmi(weight, height):
#     if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
#         return None

#     return weight / height ** 2


# rest = bmi(weight = lb_to_kg(176), height = ft_and_inch_to_m(5, 7))
# if rest == None:
#     print("Intento con valores coherentes.")
# else:
#     print(f'Your ICM is: {rest}')

def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b
 
 
def is_a_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2 
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2
print(is_a_right_triangle(5, 3, 2))
print(is_a_right_triangle(1, 3, 4))