#First Option
x = "0165031806510"
print(x.replace("0","x"))

#Second Option
for digit in "0165031806510":
    if digit == "0":
         digit = "x"
    print(digit,end="")
