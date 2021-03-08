volnePokoje = {
  9: ["Amadeus", "Goya", "Vlasy"],
  10: ["Forman", "Goya"],
  11: [],
  12: ["Amadeus", "Vlasy"]
}
a = int(input('Zadejte čas meetingů:'))
if a in volnePokoje:
    print(volnePokoje[a])
    print(f"Celkem volné {len(volnePokoje[a])} pokoje.")
else:
    print('V ten čas nejsou k dispozici volné meetingové místnosti')


