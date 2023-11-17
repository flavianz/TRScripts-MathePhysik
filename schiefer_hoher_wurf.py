import math

v0 = float(input("v0 in m/s: "))
a = float(input("Winkel in °: "))
mode = input("Starthöhe (1) oder Lochbreite (2) ? ")
if mode == "1":
    h = float(input("Starthöhe in m: "))
    v0x = v0 * math.cos(math.radians(a))

    ymax = (((v0 * math.sin(math.radians(a))) ** 2) / 19.62)  # Maximale Höhe aus v0 und alpha berechnen
    htotal = ymax + h  # Totale maximale Höhe aus y-max und Höhe
    t0 = v0 * math.sin(math.radians(a)) / 9.81  # Zeit von Start bis hälfte von Weg über y = 0
    t = t0 + (math.sqrt(2 * htotal / 9.81))  # Totale Zeit aus t0 und der Zeit
    # von hTotal zu Boden bei g = 9.81
    xmax = (float(v0) ** 2) * math.sin(math.radians(2 * float(a))) / 9.81
    xw = v0x * t  # Falldistanz aus t und v0x
    print("X-w: " + str(xw) + "\nt: " + str(t) + "\nX-max: " + str(xmax) + "\nh: " + str(htotal))
elif mode == "2":
    w = float(input("Weite in m: "))
    v0x = v0 * math.cos(math.radians(a))
    v0y = v0 * math.sin(math.radians(a))
    t = w / v0x
    h = (v0y * t) - (1 / 2 * 9.81 * (t ** 2))

