date = {}

day = int(input("Type the day: "))
month = input("Type the month: ")
year = int(input("Type the year: "))

date['dd']=day
date['month'] = month
date['aaaa'] = year

print(f"{date['dd']} de {date['month']} de {date['aaaa']}")
