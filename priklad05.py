prodeje2019 = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

prodeje2020 = {
    "Zkus mě chytit": 3157,
    "Vrah zavolá v deset": 3541,
    "Vražda podle knihy": 2510,
    "Past": 2364,
    "Zločinný steh": 5412,
}
bookName = input('Zadejte název knihy:')
if bookName in prodeje2019:
    bookSold2019 = prodeje2019[bookName]
else:
    bookSold2019 = 0

if bookName in prodeje2020:
    bookSold2020 = prodeje2020[bookName]
else:
    bookSold2020 = 0
book = bookSold2019 + bookSold2020
print(book)


