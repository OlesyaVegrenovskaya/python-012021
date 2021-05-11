import pandas
import wget

wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")
temperature = pandas.read_csv('temperature.csv')

print(temperature.head())

print(temperature.loc[temperature["Day"] == 13])

table = temperature.loc[(temperature["Day"] == 13) & (temperature["Country"] == "US")]
print(table)

print(table[(table["City"] == "Washington") | (table["City"] == "Philadelphia")])
