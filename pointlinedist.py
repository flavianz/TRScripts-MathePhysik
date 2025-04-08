import math

r = list(map(eval, input("r: ").split(",")))
s = list(map(eval, input("s: ").split(",")))
p = list(map(eval, input("p: ").split(",")))
lx = r[0]-p[0]
ly = r[1]-p[1]
lz = r[2]-p[2]
print("L("+str(r[0])+"+"+str(s[0])+"s,"+str(r[1])+"+"+str(s[1])+"s,"+ str(r[2])+"+"+str(s[2])+"s)\n")
print("->   ("+str(lx)+"+"+str(s[0])+"s)")
print("RL = ("+str(ly)+"+"+str(s[1])+"s)")
print("     ("+str(lz)+"+"+str(s[2])+"s)\n")
print("("+str(lx)+"+"+str(s[0])+"s)   ("+str(s[0])+")")
print("("+str(ly)+"+"+str(s[1])+"s) . ("+str(s[1])+") = 0")
print("("+str(lz)+"+"+str(s[2])+"s)   ("+str(s[2])+")\n")
print(str(s[0])+"("+str(lx)+"+"+str(s[0])+"s)+"+str(s[1])+"("+str(ly)+"+"+str(s[1])+"s)+"+str(s[2])+"("+str(lz)+"+"+str(s[2])+"s) = 0")
print(str(s[0] * lx+s[1] * ly+s[2] * lz)+"= -"+str(s[0] ** 2+s[1] ** 2+s[2] ** 2)+"s")
print("s = -"+str((s[0] * lx+s[1] * ly+s[2] * lz) / (s[0] ** 2+s[1] ** 2+s[2] ** 2))+"\n")
sval = -(s[0] * lx+s[1] * ly+s[2] * lz) / (s[0] ** 2+s[1] ** 2+s[2] ** 2)
print("L("+str(r[0]+sval * s[0])+","+str(r[1]+sval * s[1])+","+str(r[2]+sval * s[2])+")\n")

print("d = sqrt(("+str(r[0]+sval * s[0])+"-"+str(p[0])+")^2 + "+"("+str(r[1]+sval * s[1])+"-"+str(p[1])+")^2 + "+"("+str(r[2]+sval * s[2])+"-"+str(p[2])+")^2)")
print("d = "+str(math.sqrt((r[0]+sval * s[0] - p[0]) ** 2+(r[1]+sval * s[1] - p[1]) ** 2+(r[2]+sval * s[2] - p[2]) ** 2)))