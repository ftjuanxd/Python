gallon = 3.785411784
mile = 1.609344

def liters_100km_to_miles_gallon(liters):
    return gallon/liters * 100/mile

def miles_gallon_to_liters_100km(miles):
    return gallon/(miles*mile/100) 

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
