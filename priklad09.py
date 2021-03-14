
vysledky = [
  {"Jméno": "Mirek Dušín", "Český jazyk": 1, "Anglický jazyk": 2, "Matematika": 1, "Biologie": 1, "Zeměpis": 1},
  {"Jméno": "Jarka Metelka", "Český jazyk": 3, "Anglický jazyk": 1, "Matematika": 3, "Dějepis": 2, "Ekonomika": 5},
  {"Jméno": "Jindra Hojer", "Český jazyk": 2, "Anglický jazyk": 2, "Matematika": 1, "Biologie": 3, "Chemie": 3},
  {"Jméno": "Červenáček", "Český jazyk": 1, "Anglický jazyk": 1, "Matematika": 1, "Fyzika": 2, "Informatika": 4},
  {"Jméno": "Rychlonožka", "Český jazyk": 4, "Anglický jazyk": 3, "Matematika": 2, "Chemie": 1, "Biologie": 4},
    ]
#slovník se známkami studenta
for item in vysledky:
    marks = {}
    for items in item:
            if items != "Jméno":
                marks[items] = item[items]

def ohodnot_studenta(marks):
    sum = 0
    for key, value in marks.items():
        sum += value
        prum = sum/len(marks)
    if (prum <= 1.5 and 3 not in marks.values()):
        return "Prospěl s vyznamenáním"
    elif 5 in marks.values():
        return "Neprospěl"
    else:
        return "Prospěl"

for item in vysledky:
    name = ""
    for items in item:
        if items == "Jméno":
           name = item[items]
    print(f"{name}:{ohodnot_studenta(marks)}")