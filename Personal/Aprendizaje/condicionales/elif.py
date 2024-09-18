ingreso_mensual = 10001
gasto_mensual = 4000
if ingreso_mensual > 10000:
    if ingreso_mensual-gasto_mensual < 0:
        print("estas en deficis")
    elif ingreso_mensual-gasto_mensual >3000:
        print("estas bien")
    else:
        print("gastas un chingo")
elif ingreso_mensual > 1000:
    print("estas bien en latinoamerica")
elif ingreso_mensual > 500:
    print("estas bien en colombia")
elif ingreso_mensual > 200:
    print("estas bien en venezuela")
else:
    print("sos pobre")