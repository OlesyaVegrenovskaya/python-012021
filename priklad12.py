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


Peugeot = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
Skoda = Auto("1P3 4747", "Škoda Octavia", 41253)



car = input('Zadejte značku vozidla:')

if input == "Peugeot ":
    print(Peugeot.getInfo())
    print(Peugeot.pujc_auto())
else:
    print(Skoda.getInfo())
    print(Skoda.pujc_auto())