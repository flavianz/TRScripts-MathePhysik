r = list(map(eval, input("r: ").split(",")))
k = list(map(eval, input("k: ").split(",")))
koord = list(map(eval, input("koord: ").split(",")))

d = koord[3]

print("P(" + str(r[0]) + "+" + str(k[0]) + "k," + str(r[1]) + "+" + str(k[1]) + "k," + str(r[2]) + "+" + str(k[2]) + "k)")
print("\n" + str(koord[0]) +"(" + str(r[0]) + "+" + str(k[0]) + "k," + str(r[1]) + ")+" + str(koord[1]) + "(" + str(r[1]) + "+" + str(k[1]) + "k)+" + str(koord[2]) + "(" + str(r[2]) + "+" + str(k[2]) + "k)=" + str(d))
kval = (koord[0])*k[0]+(koord[1])*k[1]+(koord[2])*k[2]
numval = (koord[0]) * r[0] + (koord[1]) * r[1] + (koord[2]) * r[2]
print(str(numval)+"+"+str(kval)+"k="+str(d))
if kval == 0:
    print("Kein Schnittpunkt!")
else:
    print("k="+str((d-numval)/kval))