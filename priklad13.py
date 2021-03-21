class Auto:
    def __init__(self, car_plate, car_type, mileage):
        self.car_plate = car_plate
        self.car_type = car_type
        self.mileage = mileage
        self.free_auto = True

    def pujc_auto(self):
        if self.free_auto:
            self.free_auto = False
            return f"Potvrzuji zapůjčení vozidla."
        return "Vozidlo není k dispozici."

    def getInfo(self):
        if self.free_auto:
            return f"Auto {self.car_type} má registrační značku {self.car_plate}."

    def vrat_auto(self,milage_after_use, number_of_days):
        self.milage_after_use = milage_after_use
        self.number_of_days = number_of_days
        self.free_auto = True
        if number_of_days < 7:
            price = 400 * number_of_days
        else:
            price = 300 * number_of_days
        return f'Cena zapůjčení auta {self.car_type} je {price} korun'



Peugeot = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
Skoda = Auto("1P3 4747", "Škoda Octavia", 41253)

car = input('Zadejte značku vozidla:')
if input == "Peugeot ":
    print(Peugeot.getInfo())
    print(Peugeot.pujc_auto())
else:
    print(Skoda.getInfo())
    print(Skoda.pujc_auto())

if car == "Peugeot" or car == "Škoda":
    milage_after_use = int(input('Zadejte stav tachometru:'))
    number_of_days = int(input('Zadejte počet dnů:'))
    if car == "Peugeot":
        print(Peugeot.vrat_auto(milage_after_use, number_of_days))
    if car == "Škoda":
        print(Skoda.vrat_auto(milage_after_use, number_of_days))

