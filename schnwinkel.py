import math

mode = input("GG(1), GE(2) oder EE(3): ")
if mode == "1":
    s = list(map(eval, input("s: ").split(",")))
    t = list(map(eval, input("t: ").split(",")))
    val = math.fabs(s[0] * t[0] + s[1] * t[1] + s[2] * t[2]) / (math.sqrt(s[0] ** 2 + s[1] ** 2 + s[2] ** 2) * math.sqrt(t[0] ** 2 + t[1] ** 2 + t[2] ** 2))
    print("       " + str(s[0]) + " " + str(t[0]))
    print("       " + str(s[1]) + "." + str(t[1]))
    print("       " + str(s[2]) + " " + str(t[2]))
    print("cos(a)=--------- = "+str(val)+" => a="+str(math.degrees(math.acos(val))))
    print("       |" + str(s[0]) + "| |" + str(t[0]))
    print("       |" + str(s[1]) + "|.|" + str(t[1]))
    print("       |" + str(s[2]) + "| |" + str(t[2]))
elif mode == "2":
    koord = list(map(eval, input("koord: ").split(",")))
    t = list(map(eval, input("t: ").split(",")))
    val = math.fabs(koord[0] * t[0] + koord[1] * t[1] + koord[2] * t[2]) / (
            math.sqrt(koord[0] ** 2 + koord[1] ** 2 + koord[2] ** 2) * math.sqrt(t[0] ** 2 + t[1] ** 2 + t[2] ** 2))
    print("                    " + str(koord[0]) + " " + str(t[0]))
    print("                    " + str(koord[1]) + "." + str(t[1]))
    print("          |n.RV|    " + str(koord[2]) + " " + str(t[2]))
    print("cos(90-a)=--------=----- = " + str(val) + " => a=" + str(-(math.degrees(math.acos(val))-90)))
    print("          |n|.|RV| |" + str(koord[0]) + "| |" + str(t[0]))
    print("                   |" + str(koord[1]) + "|.|" + str(t[1]))
    print("                   |" + str(koord[2]) + "| |" + str(t[2]))
else:
    koord1 = list(map(eval, input("koord1: ").split(",")))
    koord2 = list(map(eval, input("koord2: ").split(",")))
    val = math.fabs(koord1[0] * koord2[0] + koord1[1] * koord2[1] + koord1[2] * koord2[2]) / (
                math.sqrt(koord1[0] ** 2 + koord1[1] ** 2 + koord1[2] ** 2) * math.sqrt(koord2[0] ** 2 + koord2[1] ** 2 + koord2[2] ** 2))
    print("       " + str(koord1[0]) + " " + str(koord2[0]))
    print("       " + str(koord1[1]) + "." + str(koord2[1]))
    print("       " + str(koord1[2]) + " " + str(koord2[2]))
    print("cos(a)=--------- = " + str(val) + " => a=" + str(math.degrees(math.acos(val))))
    print("       |" + str(koord1[0]) + "| |" + str(koord2[0]))
    print("       |" + str(koord1[1]) + "|.|" + str(koord2[1]))
    print("       |" + str(koord1[2]) + "| |" + str(koord2[2]))