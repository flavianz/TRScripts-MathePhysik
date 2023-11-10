import math

mode = input("Distanzen (d / 1), Winkel (w / 2) oder Geschwindigkeit (g / 3) ? ")

if mode == "d" or mode == "D" or mode == "1":
    v0 = float(input("V0 in m/s: "))
    winkel = float(input("Winkel in °: "))
    ymax = ((v0 * math.sin(math.radians(winkel))) ** 2) / (9.81 * 2)
    xw = (v0 ** 2) * math.sin(2 * math.radians(winkel)) / 9.81

    print("Y-max: " + str(ymax) + " m\nX-w: " + str(xw) + " m")
if mode == "w" or mode == "W" or mode == "2":
    vorhanden = input("Vorhanden: Y-max (y / 1) oder X-w (x / 2) ? ")
    if vorhanden == "y" or vorhanden == "Y" or vorhanden == "1":
        
