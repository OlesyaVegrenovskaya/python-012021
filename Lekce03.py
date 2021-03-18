class Book:
    def __init__(self, title, pages, price):
        self.title = title
        self.pages = pages
        self.price = price

    def getInfo(self):
        return f'Kniha {self.title} je zajimava a stoji {self.price} Kč'

    def discount(self, sleva):
        self.price -= self.price * (sleva/100)

kniha = Book('Harry poter', 350 ,250)
print(kniha.getInfo())
kniha.discount(30)
print(kniha.getInfo())

class Package:
    def __init__(self, address, weightInKilos):
        self.address = address
        self.weightInKilos = weightInKilos
        self.delivered = False

    def deliver(self):
        self.delivered = True

    def getInfo(self):
        if self.delivered:
             return f'Balik byl doručen do adresy {self.address}. Hmotnost zasilky je {self.weightInKilos} a zasilka byla doručena.'
        else:
            return f'Balik ne byl doru4en na adresu {self.address}. Hmotnost zasilky je {self.weightInKilos}'

Zasilka = Package('Pod Harfou 981/27', 27)
print(Zasilka.getInfo())
Zasilka.deliver()
print(Zasilka.getInfo())

class Employee:
    def getInfo(self):
        return f'{self.name} pracuje na pozici {self.position}.'

frantisek = Employee()
frantisek.name = "František Novák"
frantisek.position = "konstruktér"
print(frantisek.getInfo())

klara = Employee()
klara.name = "Klára Nová"
klara.position = "konstrukterka"
print(frantisek.getInfo())
print(klara.getInfo())

class Employee:
  def getInfo(self):
    return f"{self.name} pracuje na pozici {self.position}."
  def __init__(self, name, position):
    self.name = name
    self.position = position

frantisek = Employee("František Novák", "konstrukter")
klara = Employee("Klára Nová", "svářec")

print(frantisek.getInfo())
print(klara.getInfo())
