class Auto:
    def __init__(self, car_plate, car_type, mileage):
        self.car_plate = car_plate
        self.car_type = car_type
        self.mileage = mileage
        self.free_auto = True

    def free_auto(self):
        self.free_auto = False

    def getInfo(self):
        if self.free_auto:
            return f"Auto {self.car_type}  která má registrační značku {self.car_plate} a {self.mileage} počet najetých kilometrů je k dispozici"
        return f"Auto {self.car_type} která má registrační značku {self.car_plate} a {self.mileage} počet najetých kilometrů neni k dispozici"


Peugeot = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
Skoda = Auto("1P3 4747", "Škoda Octavia", 41253)

print(Peugeot.getInfo())
print(Skoda.getInfo())