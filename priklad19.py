from forex_python.converter import CurrencyRates
prevodnik = CurrencyRates()
pozadovano_v_cilove_mene = int(input("Zadejte častku ve měně USD:"))
cena_v_korunach = prevodnik.convert('USD', 'CZK', pozadovano_v_cilove_mene)
print(cena_v_korunach)

from forex_python.converter import CurrencyRates
prevodnik = CurrencyRates()
pozadovano_v_cilove_mene = int(input("Zadej částku ve měně EUR: "))
cena_v_korunach = prevodnik.convert('EUR', 'CZK', pozadovano_v_cilove_mene)
print(cena_v_korunach)

from forex_python.converter import CurrencyRates
prevodnik = CurrencyRates()
pozadovano_v_cilove_mene = int(input("Zadej částku ve měně DKK: "))
cena_v_korunach = prevodnik.convert('DKK', 'CZK', pozadovano_v_cilove_mene)
print(cena_v_korunach)