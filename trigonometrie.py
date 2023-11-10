import math

while True:
    version = input("Theorie (t / 1) oder Rechner (r / 2)? ")

    if version == "t" or version == "T" or version == "1":
        print("\nSinus = (Gegenkathete / Hypotenuse)"
              "\nCosinus = (Ankathete / Hypotenuse)"
              "\nTangens = (Gegenkathete / Ankathete)")
    else:
        art = input("Winkel (w / 1) oder Seite (s / 2) finden? ")

        if art == "w" or art == "W" or art == "1":
            gegenkathete = float(input("Länge Gegenkathete: "))
            ankathete = float(input("Länge Ankathete: "))
            winkel = math.degrees(math.atan(gegenkathete / ankathete))
            print("\nRechenweg: tan-1(Gegenkathete / Ankathete) = tan-1("
                  + str(gegenkathete) + " / " + str(ankathete) + ")")
            print("Winkel: " + str(winkel) + "\n\n")
        else:
            seite = input("Gegenüber (g / 1), an Winkel (w / 2) "
                          "oder Hypotenuse (h / 3) ? ")
            winkel = float(input("Winkel: "))
            if seite == "g" or seite == "G" or seite == "1":
                hypotenuse = float(input("Länge Hypotenuse: "))
                length = math.sin(math.radians(winkel))
                print("\nRechenweg: sin(Winkel) * Hypotenuse = sin("
                      + str(winkel) + ") * " + str(hypotenuse))
                print("Gegenüberliegende Seite: " + str(length * hypotenuse) + "\n\n")
            elif seite == "w" or seite == "W" or seite == "2":
                hypotenuse = float(input("Länge Hypotenuse: "))
                length = math.cos(math.radians(winkel))
                print("\nRechenweg: cos(Winkel) * Hypotenuse = cos("
                      + str(winkel) + ") * " + str(hypotenuse))
                print("Anliegende Seite: " + str(length * hypotenuse) + "\n\n")
            else:
                seite_vorhanden = input("Vorhandene Seite "
                                        "(Ankathete (a / 1), Gegenkathete (g / 2): ")
                if (seite_vorhanden == "a" or
                        seite_vorhanden == "A" or seite_vorhanden == "1"):
                    ankathete = float(input("Länge Ankathete: "))
                    hypotenuse = ankathete / (math.cos(math.radians(winkel)))
                    print("\nRechenweg: Ankathete / cos(Winkel) = "
                          + str(ankathete) + " / cos(" + str(winkel) + ")")
                    print("Länge Hypotenuse: " + str(hypotenuse) + "\n\n")
                else:
                    gegenkathete = float(input("Länge Gegenkathete: "))
                    hypotenuse = gegenkathete / math.sin(math.radians(winkel))
                    print("\nRechenweg: Gegenkathete / sin(Winkel) = "
                          + str(gegenkathete) + " / sin(" + str(winkel) + ")")
                    print("Länge Hypotenuse: " + str(hypotenuse) + "\n\n")
