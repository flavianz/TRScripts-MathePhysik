r1 = list(map(eval, input("r1: ").split(",")))
s = list(map(eval, input("s: ").split(",")))
r2 = list(map(eval, input("r2: ").split(",")))
t = list(map(eval, input("t: ").split(",")))

print(str(s[0]) + "   " + str(t[0]) + "   " + str(s[1] * t[2]) + " - " + str(s[2] * t[1]) + "   " + str(s[1] * t[2] - s[2] * t[1]))
print(str(s[1]) + " x " + str(t[1]) + " = -" + str(s[0] * t[2]) + " + " + str(s[2] * t[0]) + " = " + str(-s[0] * t[2] + s[2] * t[0]))
print(str(s[2]) + "   " + str(t[2]) + "   " + str(s[0] * t[1]) + " - " + str(s[1] * t[0]) + "   " + str(s[0] * t[1] - s[1] * t[0]))

print("x=|BA|.cos(a)=|BA|.((BA.n)/(|BA|.|n|))=BA.(n/|n|)")