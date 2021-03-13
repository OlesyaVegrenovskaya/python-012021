def number_control(number):
    if len(number) == 13 and number[0:4] == "+420":
        return True
    elif len(number) == 9 and number[0:4] != "+420":
        number = "+420" + number
        return True
    else:
        return False


def priceText(text):
    letter = 3
    price = round((letter * (len(text) / 180)), 1)
    if price < 1:
        price = 1
    print(f"Cena textu je {price} korun.")


number = input("Zadejte telefonni čislo:")
number = number.replace(" ", "")
if number_control(number) == True:
       text = input("Zadejte text:")
       priceText(text)
else:
    print("Zadejte správni telefonní čislo.")
