import math

def is_empty(val):
    return val == "" or val == " "


mode = input("Bei bestimmtem Wert? (1: ja / 2: nein) ")

if mode == "1" or mode == "1 ":
    v0 = float(input("v0 in m/s: "))
    winkel = float(input("Winkel in °: "))
    v0x = v0 * math.cos(math.radians(winkel))
    v0y = v0 * math.sin(math.radians(winkel))
    var = input("Zeit (1), x (2)? ")
    t = 0
    if var == "1":
        t = float(input("Zeit in s: "))
    elif var == "2":
        x = float(input("x in m: "))
        t = x / v0x
    v = math.sqrt((v0x ** 2) + ((v0y - 9.81 * t) ** 2))
    vy = v0 * math.sin(math.radians(winkel)) - 9.81 * t
    winkelt = math.degrees(math.atan(vy / v0x))
    x = v0 * math.cos(math.radians(winkel)) * t
    y = v0 * math.sin(math.radians(winkel)) * t - (1 / 2) * 9.81 * (t ** 2)
    print(f"\nv: {str(v)}\na: {str(winkelt)}\nx: {str(x)}\ny: {str(y)}\nVy: {str(vy)}\nVx: {str(v0x)}\nV0y: {str(v0y)}\nV0x: {str(v0x)}\nt: {str(t)}\n")

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
                print(f"\nv0 = sqrt({xw} * 9.81 / sin(2 * {winkel}))")
            elif not is_empty(ymax):
                sin = math.sin(math.radians(float(winkel)))
                sqrt = math.sqrt(float(ymax) * 19.62)
                v0 = sqrt / sin
                print(f"\nv0 = sqrt({ymax} * 19.62 / sin({winkel}))")
            elif not is_empty(t):
                v0 = (float(t) * 9.81) / (2 * math.sin(math.radians(float(winkel))))
                print(f"\nv0 = ({t} * 9.81) / (2 * sin({winkel}))")
    if is_empty(winkel):
        if is_empty(v0):
            winkel = ""
        else:
            if not is_empty(xw):
                inner = float(xw) * 9.81 / (float(v0) ** 2)
                winkel = math.degrees(math.asin(inner)) / 2
                print(f"\na = (sin-1(({xw} * 9.81) / ({v0} ^ 2))")
            elif not is_empty(ymax):
                sqrt = math.sqrt(float(ymax) * 19.62)
                winkel = math.degrees(math.asin(sqrt / float(v0)))
                print(f"\na = sin-1((sqrt({ymax} * 19.62) / {v0})")
            elif not is_empty(t):
                inner = (float(t) * 9.81) / (2 * float(v0))
                winkel = math.degrees(math.asin(inner))
                print(f"\na = sin-1(({t} * 9.81) / (2 * {v0}))")
    if is_empty(t):
        if not is_empty(v0) and not is_empty(winkel):
            t = 2 * float(v0) * math.sin(math.radians(float(winkel))) / 9.81
            print(f"\nt = 2 * {v0} * sin({winkel}) / 9.81")
    if is_empty(ymax):
        if not is_empty(v0) and not is_empty(winkel):

            ymax = (((float(v0) * math.sin(math.radians(float(winkel)))) ** 2) / 19.62)
            print(f"\nY-max = {v0} * (sin({winkel}) ^ 2) / 19.62")
    if is_empty(xw):
        if not is_empty(v0) and not is_empty(winkel):
            xw = (float(v0) ** 2) * math.sin(math.radians(2 * float(winkel))) / 9.81
            print(f"\nx-w = ({v0} ^ 2) * sin(2 * {winkel}) / 9.81")


    print(f"\nv0: {str(v0)}\na: {str(winkel)}\nt: {str(t)}\nY-max: {str(ymax)}\nX-w: {str(xw)}")