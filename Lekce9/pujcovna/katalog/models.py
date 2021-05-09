from django.db import models

# Create your models here.
class Auto(models.Model):
    registracni_znacka = models.CharField(max_length=20)
    znacka_typ = models.CharField(max_length=100)
    pocet_km = models.IntegerField()
    datum_tech_kontroly = models.DateField()


class Zakaznik(models.Model):
    jmeno_a_prijmeni = models.CharField(max_length=100)
    cislo_ridicskeho_prukazu = models.CharField(max_length=100)
    datum_narozeni = models.DateField()

class Vypujcka(models.Model):
    datum_a_cas_zacatek_vypujcky = models.DateField()
    datum_a_cas_konec_vypujcky = models.DateField()
    cena_vypujcky = models.IntegerField()



