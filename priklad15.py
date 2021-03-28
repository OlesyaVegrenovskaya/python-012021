from datetime import datetime, timedelta

date = input('Zadejte datum:')
time = datetime.strptime(date, "%d.%m.%Y")
people = int(input('Zdadejte počet osob:'))

first_date = datetime(2021, 7, 1)
second_date = datetime(2021, 8, 11)
third_date = datetime(2021, 8, 31)

if first_date <= time < second_date:
    price = people*250
    print(f'Cena vstupenek je {price}.')
elif second_date <= time <= third_date:
    price = people*180
    print(f'Cena vstupenek je {price}.')
else:
    print(f'Letní kino je v té době uzavřené.')
