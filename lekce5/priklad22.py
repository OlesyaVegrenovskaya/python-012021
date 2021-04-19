import pandas
import wget
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/character-deaths.csv")

character_deaths = pandas.read_csv("character-deaths.csv")
character_deaths = character_deaths.set_index("Name")
print(character_deaths.columns)
print(character_deaths.loc["Hali", "Death Year"])
print(character_deaths.loc["Gevin Harlaw": "Gillam"])
print(character_deaths.loc["Gevin Harlaw":"Gillam", "Death Year"])
print(character_deaths.loc["Gevin Harlaw":"Gillam", "GoT":"DwD"])