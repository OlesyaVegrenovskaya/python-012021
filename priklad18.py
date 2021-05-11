from datetime import datetime, timedelta

class Kontakt:
  def __init__(self, jmeno, email):
    self.jmeno = jmeno
    self.email = email

class Uchacez(Kontakt):
    def __init__(self, jmeno, email, datum_pohovoru):
        super().__init__(jmeno, email)
        self.datum_pohovoru = datetime.strptime(datum_pohovoru, "%d. %m. %Y")
        self.zapis_z_pohovoru = ""

    def uloz_zapis(self, zapis):
        if datetime.now() < self.datum_pohovoru:
            return f"Pohovor ještě neproběhl."
        else:
            self.zapis_z_pohovoru = zapis
            return f"Zápis z pohovoru byl uložen."

pohovor1 = Uchacez("Olesya Vegrenovskaya", "veg@seznam.cz", "21. 5. 2021")
pohovor2 = Uchacez("Dominik Burdenkov", "domca@seznam.cz", "01. 03. 2021")

print(pohovor1.uloz_zapis("xxxxxxx"))
print(pohovor2.uloz_zapis("xxxxxxxx"))

