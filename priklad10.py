def chances_for_success(industry, turnover, state, conference=False, newsletter=False):
    points = 0
    if industry == "automotive":
        points += 3
    elif industry == "retail":
        points += 2
    else:
        points += 0

    if turnover < 10000000:
        points += 0
    elif 10000000 <= turnover <= 100000000:
        points += 3
    else:
        points += 1

    if state == "Česko" or "Slovensko":
        points += 2
    elif state == "Německo" or "Francie":
        points += 1
    else:
        points += 0

    if conference:
        points += 1
    else:
        points += 0

    if newsletter:
        points += 1
    else:
        points += 0

    if points < 5:
        print("Šance na záskání je malá.")
    if 5 <= points <= 8:
        print("Šance na získání je střední.")
    else:
        print("Šance na získání je vysoká.")


industry_input = input("Zadejte odvětvi:")
turnover_input = int(input("Zadejte obrat:"))
state_input = input("Zadejte zemi:")
conference_input = input("Účast na konferenci(Ano/Ne):")
newsletter_input = input("Odběr newsletteru(Ano/Ne):")

if conference_input == "Ano":
    if newsletter_input == "Ano":
        chances_for_success(industry_input, turnover_input, state_input, True, True)
    else:
        chances_for_success(industry_input, turnover_input, state_input, True, False)
else:
    if newsletter_input == "Ano":
        chances_for_success(industry_input, turnover_input, state_input, False, True)
    else:
        chances_for_success(industry_input, turnover_input, state_input, False, False)
