import pandas
import wget
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/country_vaccinations.csv")
country = pandas.read_csv("country_vaccinations.csv")

total_vaccinated = country.loc[(country["date"] == "2021-03-10"), ["country", "total_vaccinations"]]
print(total_vaccinated)

million = country.loc[(country["date"] == "2021-03-10") & (country["total_vaccinations"] > 1_000_000), ["country", "total_vaccinations"]]
print(million)

more_than_thousand = country.loc[(country["date"] == "2021-03-10") & (country["daily_vaccinations"] > 100_000)]
print(more_than_thousand)

less_than_thousand = country.loc[(country["date"]== "2021-03-10") & (country["daily_vaccinations"] < 100_000)]
print(less_than_thousand)