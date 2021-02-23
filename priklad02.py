sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}
a = input('Zadejte kód součástky:')
if a in sklad:
  b = str(input('Zadejte množství :'))
  if b > str(sklad.get(a)):
       print('Lze prodat pouze ' + str(sklad[a]) +' kusů.')
       del sklad[a]
  else:
    print('Poptávku lze uspokojit v plné výši')
    c = str(sklad.get(a))-b
    sklad[a]=c
else:
  print('Součástka není skladem.')
