sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}
a = input('Zadejte kód součástky:')
if a in sklad:
  b = int(input('Zadejte množství :'))
  if b > int(sklad.get(a)):
       print('Lze prodat pouze ' + str(sklad[a]) +' kusů.')
       del sklad[a]
        print(sklad)
  else:
    print('Poptávku lze uspokojit v plné výši')
    c = int(sklad.get(a))-b
    sklad[a]=c
    print(sklad)
else:
  print('Součástka není skladem.')
