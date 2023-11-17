import math

from_type = input("Steigung (1), % (2) oder Winkel (3) ? ")
to = input("m (1), % (2) oder Winkel (3) ? ")
val = float(input("Wert: "))

if from_type == "1":
    if to == "2":
        print("Prozent = " + str(val * 200))
    else:
        print("Winkel = " + str(math.degrees(math.atan(val))))
