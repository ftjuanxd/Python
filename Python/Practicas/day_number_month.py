def leap_year(year):
    if year < 1582 or year%4 != 0:
        return False
    elif year%100 != 0:
        return True
    elif year%400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and leap_year(year):
        return 29
    else:
        return days[month - 1]

def day_of_year(year, month, day):
    days = 0
    for i in range(1, month):
        days += days_in_month(year, i)
    days += day
    return days
    
test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"->",end="")
    result = leap_year(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
print(day_of_year(2000,12,31))
