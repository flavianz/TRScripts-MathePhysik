import math

mode = input("Distanzen (d / 1), Winkel (w / 2) oder Geschwindigkeit (g / 3) ? ")

def is_empty(val):
    return val == "" or val == " "

if mode == "d" or mode == "D" or mode == "1":
    v0 = input("V0 in m/s: ")
    winkel = input("Winkel in °: ")
    t = input("Zeit in s: ")
    ymax = input("Y-max in m: ")
    xw = input("X-w in m: ")
    if is_empty(v0):
        if is_empty(winkel):
            print("Benötige Winkel zur Kalkulation der Seite")
        else:
            if not is_empty(xw):
                v0 = math.sqrt(float(xw) * 9.81 /
                               math.sin(math.radians(2 * float(winkel))))
                print(f"\nV0 = sqrt({xw} * 9.81 / sin(2 * {winkel}))\n" +
                      f"V0 = {v0}")

