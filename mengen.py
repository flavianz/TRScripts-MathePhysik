avogadro = 6.022 * 10 ** 23
unit_from = input("Von u, g, mol (m)?")
weight = float(input(unit_from + ": "))
grams = weight
if unit_from == "u":
    grams = weight / avogadro
elif unit_from == "m" or unit_from == "mol":
    molare_masse = float(input("Molare Masse (g/mol): "))
    grams = weight * molare_masse

to = input("Zu u, g oder mol (m)?")

if to == "u":
    print(str(weight) + unit_from + " = " + str(grams * avogadro) + "u")
elif to == "g":
    print(str(weight) + unit_from + " = " + str(grams) + "g")
else:
    molare_masse = float(input("Molare Masse (g/mol): "))
    print(str(weight) + unit_from + " = " + str(grams / molare_masse) + "mol")