import pandas
import wget
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/country_vaccinations.csv")
country = pandas.read_csv("country_vaccinations.csv")
