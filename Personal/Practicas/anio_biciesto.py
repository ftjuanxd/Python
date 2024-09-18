year = int(input("Type year: "))
if year < 1582:
    print("No dentro del período del calendario Gregoriano")
elif year%4 != 0:
    print("Anio Comun. ")
elif year%100 != 0:
    print("Anio Biciesto. ")
elif year%400 != 0:
    print("Anio Comun. ")
else:
    print("Anio Biciesto. ")