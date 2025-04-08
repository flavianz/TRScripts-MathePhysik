r = list(map(eval, input("r: ").split(",")))
s = list(map(eval, input("s: ").split(",")))
t = list(map(eval, input("t: ").split(",")))

print("-> " + str(s[0]) + "   " + str(t[0]) + "   " + str(s[1] * t[2]) + " - " + str(s[2] * t[1]) + "   " + str(s[1] * t[2] - s[2] * t[1]))
print("n =" + str(s[1]) + " x " + str(t[1]) + " = -" + str(s[0] * t[2]) + " + " + str(s[2] * t[0]) + " = " + str(-s[0] * t[2] + s[2] * t[0]))
print("   " + str(s[2]) + "   " + str(t[2]) + "   " + str(s[0] * t[1]) + " - " + str(s[1] * t[0]) + "   " + str(s[0] * t[1] - s[1] * t[0]))

d = (s[1] * t[2] - s[2] * t[1]) * r[0] + (-s[0] * t[2] + s[2] * t[0]) * r[1] + (s[0] * t[1] - s[1] * t[0]) * r[2]
print("\n"+str(s[1] * t[2] - s[2] * t[1])+"x+"+str(-s[0] * t[2] + s[2] * t[0])+"y+"+str(s[0] * t[1] - s[1] * t[0])+"z="+str(d))