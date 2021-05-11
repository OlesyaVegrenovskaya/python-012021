import wget
import pandas


wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")
temperature = pandas.read_csv('temperature.csv')

print(temperature.head())

prague = temperature[(temperature["City"] == "Prague")]
print(prague)

more_than_eighty = temperature[(temperature["AvgTemperature"] > 80)]
print(more_than_eighty)

more_than_sixty = temperature[(temperature["AvgTemperature"] > 60) & (temperature["Region"] == "Europe")]
print(more_than_sixty)

high_low = temperature[(temperature["AvgTemperature"] < -20) | (temperature["AvgTemperature"] > 80)]
print(high_low)

