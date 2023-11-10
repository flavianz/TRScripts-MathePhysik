import math

while True:
    version = input("Theorie (t / 1) oder Rechner (r / 2)? ")

    if version == "t" or version == "T" or version == "1":
        print("\nSinus = (Gegenkathete / Hypothenuse)"
              "\nCosinus = (Ankathete / Hypothenuse)"
              "\nTangens = (Gegenkathete / Ankathete)")
    else:
        art = input("Winkel (w / 1) oder Seite (s / 2) finden? ")

        if art == "w" or art == "W" or art == "1":
            gegenkathete = float(input("Länge Gegenkathete: "))
            ankathete = float(input("Länge Ankathete: "))
            winkel = math.degrees(math.atan(gegenkathete / ankathete))
            print("\nRechenweg: tan-1(Gegnkathete / Ankathete) = tan-1("
                  + str(gegenkathete) + " / " + str(ankathete) + ")")
            print("Winkel: " + str(winkel) + "\n\n")
        else:
            seite = input("Gegenüber (g / 1), an Winkel (w / 2) "
                          "oder Hypothenuse (h / 3) ? ")
            winkel = float(input("Winkel: "))
            if seite == "g" or seite == "G" or seite == "1":
                hypothenuse = float(input("Länge Hypothenuse: "))
                length = math.sin(math.radians(winkel))
                print("\nRechenweg: sin(Winkel) * Hypothenuse = sin("
                      + str(winkel) + ") * " + str(hypothenuse))
                print("Gegenüberliegende Seite: " + str(length * hypothenuse) + "\n\n")
            elif seite == "w" or seite == "W" or seite == "2":
                hypothenuse = float(input("Länge Hypothenuse: "))
                length = math.cos(math.radians(winkel))
                print("\nRechenweg: cos(Winkel) * Hypothenuse = cos("
                      + str(winkel) + ") * " + str(hypothenuse))
                print("Anliegende Seite: " + str(length * hypothenuse) + "\n\n")
            else:
                seite_vorhanden = input("Vorhandene Seite "
                                        "(Ankathete (a / 1), Gegenkathete (g / 2): ")
                if (seite_vorhanden == "a" or
                        seite_vorhanden == "A" or seite_vorhanden == "1"):
                    ankathete = float(input("Länge Ankathete: "))
                    hypothenuse = ankathete / (math.cos(math.radians(winkel)))
                    print("\nRechenweg: Ankathete / cos(Winkel) = "
                          + str(ankathete) + " / cos(" + str(winkel) + ")")
                    print("Länge Hypothenuse: " + str(hypothenuse) + "\n\n")
                else:
                    gegenkathete = float(input("Länge Gegenkathete: "))
                    hypothenuse = gegenkathete / math.sin(math.radians(winkel))
                    print("\nRechenweg: Gegenkathete / sin(Winkel) = "
                          + str(gegenkathete) + " / sin(" + str(winkel) + ")")
                    print("Länge Hypothenuse: " + str(hypothenuse) + "\n\n")
