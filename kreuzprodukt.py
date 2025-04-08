v1 = list(map(eval, input("v1: ").split(",")))
v2 = list(map(eval, input("v1: ").split(",")))

print(str(v1[0]) + "   " + str(v2[0]) + "   " + str(v1[1] * v2[2]) + " - " + str(v1[2] * v2[1]) + "   " + str(v1[1] * v2[2] - v1[2] * v2[1]))
print(str(v1[1]) + " x " + str(v2[1]) + " = -" + str(v1[0] * v2[2]) + " + " + str(v1[2] * v2[0]) + " = " + str(-v1[0] * v2[2] + v1[2] * v2[0]))
print(str(v1[2]) + "   " + str(v2[2]) + "   " + str(v1[0] * v2[1]) + " - " + str(v1[1] * v2[0]) + "   " + str(v1[0] * v2[1] - v1[1] * v2[0]))