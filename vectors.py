import math

while(True):
    veca = input("Vektor a: ")
    ax = float(veca.split(",")[0])
    ay = float(veca.split(",")[1])
    az = float(veca.split(",")[2])
    vecb = input("Vektor b: ")
    bx = float(vecb.split(",")[0])
    by = float(vecb.split(",")[1])
    bz = float(vecb.split(",")[2])

    product = ax * bx + ay * by + az * bz
    absa = math.sqrt(ax ** 2 + ay ** 2 + az ** 2)
    absb = math.sqrt(bx ** 2 + by ** 2 + bz ** 2)
    angle = math.degrees(math.acos(product / (absa * absb)))

    print("\nBetrag a: " + str(absa) + "\nBetrag b: " + str(absb) + "\nProdukt: " + str(product) + "\nWinkel: " + str(angle) + "\n\n")

