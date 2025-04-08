import math

while True:
    a = eval(input("a: "))
    if a == 0:
        print("Lösungen (0):")
        continue

    b = eval(input("b: "))
    c = eval(input("c: "))

    diskriminante = b ** 2 - 4 * a * c

    if diskriminante < 0:
        print("Lösungen (0):")
        continue

    if diskriminante == 0:
        sol1 = -b / (2 * a)
        print("Lösungen (1):\n" + str(sol1))
        continue

    sol1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    sol2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)

    print("Lösungen (2):\n" + str(sol1) + "\n" + str(sol2))