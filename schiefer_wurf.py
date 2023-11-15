import math


def is_empty(val):
    return val == "" or val == " "


while True:
    mode = input("Bei bestimmtem Wert? (1: ja / 2: nein) ")

    if mode == "1" or mode == "1 ":
        v0 = float(input("v0 in m/s: "))
        winkel = float(input("Winkel in °: "))
        v0x = v0 * math.cos(math.radians(winkel))
        v0y = v0 * math.sin(math.radians(winkel))
        print("\nv0x = cos(" + str(winkel) + ")\n")
        var = input("Zeit (1), x (2) oder Winkel (3)? ")
        t = 0
        if var == "1":
            t = float(input("Zeit in s: "))
        elif var == "2":
            x = float(input("x in m: "))
            t = x / v0x
        elif var == "3":
            zwinkel = float(input("Zielwinkel in °: "))
            root_val = (v0 * math.sin(zwinkel)) ** 2
            print(root_val)
            t = (-1 * v0 * math.sin(zwinkel) + math.sqrt(root_val)) / 9.81
            print(t)
        v = math.sqrt((v0x ** 2) + ((v0y - 9.81 * t) ** 2))
        vy = v0 * math.sin(math.radians(winkel)) - 9.81 * t
        winkelt = math.degrees(math.atan(vy / v0x))
        x = v0 * math.cos(math.radians(winkel)) * t
        y = v0 * math.sin(math.radians(winkel)) * t - (1 / 2) * 9.81 * (t ** 2)
        print("\nv: " + str(v) + "\na: " + str(winkelt) + "\nx: " + str(x) + "\ny: " + str(y) + "\nVy: " +
              str(vy) + "\nVx: " + str(v0x) + "\nV0y: " + str(v0y) + "\nV0x: " + str(v0x) + "\nt: " + str(t) + "\n")

    else:
        v0 = input("v0 in m/s: ")
        winkel = input("Winkel in °: ")
        t = input("Zeit in s: ")
        ymax = input("Y-max in m: ")
        xw = input("X-w in m: ")
        if is_empty(v0):
            if is_empty(winkel):
                v0 = ""
            else:
                if not is_empty(xw):
                    sin = math.sin(2 * math.radians(float(winkel)))
                    v0 = math.sqrt(float(xw) * 9.81 / sin)
                    print("\nv0 = sqrt(" + str(xw) + " * 9.81 / sin(2 * " + str(winkel) + "))")
                elif not is_empty(ymax):
                    sin = math.sin(math.radians(float(winkel)))
                    sqrt = math.sqrt(float(ymax) * 19.62)
                    v0 = sqrt / sin
                    print("\nv0 = sqrt(" + str(ymax) + " * 19.62 / sin(" + str(winkel) + "))")
                elif not is_empty(t):
                    v0 = (float(t) * 9.81) / (2 * math.sin(math.radians(float(winkel))))
                    print("\nv0 = (" + str(t) + " * 9.81) / (2 * sin(" + str(winkel) + "))")
        if is_empty(winkel):
            if is_empty(v0):
                winkel = ""
            else:
                if not is_empty(xw):
                    inner = float(xw) * 9.81 / (float(v0) ** 2)
                    winkel = math.degrees(math.asin(inner)) / 2
                    print("\na = (sin-1((" + str(xw) + " * 9.81) / (" + str(v0) + " ^ 2))")
                elif not is_empty(ymax):
                    sqrt = math.sqrt(float(ymax) * 19.62)
                    winkel = math.degrees(math.asin(sqrt / float(v0)))
                    print("\na = sin-1((sqrt(" + str(ymax) + " * 19.62) / " + str(v0) + ")")
                elif not is_empty(t):
                    inner = (float(t) * 9.81) / (2 * float(v0))
                    winkel = math.degrees(math.asin(inner))
                    print("\na = sin-1((" + str(t) + " * 9.81) / (2 * " + str(v0) + "))")
        if is_empty(t):
            if not is_empty(v0) and not is_empty(winkel):
                t = 2 * float(v0) * math.sin(math.radians(float(winkel))) / 9.81
                print("\nt = 2 * " + str(v0) + " * sin(" + str(winkel) + ") / 9.81")
        if is_empty(ymax):
            if not is_empty(v0) and not is_empty(winkel):
                ymax = (((float(v0) * math.sin(math.radians(float(winkel)))) ** 2) / 19.62)
                print("\nY-max = " + str(v0) + " * (sin(" + str(winkel) + ") ^ 2) / 19.62")
        if is_empty(xw):
            if not is_empty(v0) and not is_empty(winkel):
                xw = (float(v0) ** 2) * math.sin(math.radians(2 * float(winkel))) / 9.81
                print("\nx-w = (" + v0 + " ^ 2) * sin(2 * " + winkel + ") / 9.81")
        print("\nv0: " + str(v0) + "\na: " + str(winkel) + "\nt: " + str(t) + "\nY-max: " +
              str(ymax) + "\nX-w: " + str(xw) + "")
