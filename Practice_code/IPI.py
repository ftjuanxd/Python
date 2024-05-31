ingreso = float(input('Type your income: '))
impuesto = float()
cifra = 85528
if ingreso > cifra:
    impuesto = (ingreso-cifra) *.32+ 14839.02
else:
    impuesto  = ingreso * .18- 556.02
impuesto = round(impuesto,0)
if impuesto < 0: impuesto = 0.0
print(f"El impuesto es: {impuesto} pesos")
