while True:
    mode = input("u zu Gramm (1) oder Gramm zu u (2)? ")
    u_to_g = 1.66 * (10 ** -24)
    g_to_u = 6.02 * (10 ** 23)
    if mode == "2":
        g = input("Gramm: ")
        print("u = " + str(g) + " * 6.02 * 10^23")
        print("u: " + str(float(g) * g_to_u))
        print("u: " + str(float(g) * 6.02) + " * 10^23")
    else:
        u = input("U: ")
        print("g = " + str(u) + " * 1.66 * 10^-24")
        print("g: " + str(float(u) * u_to_g))
        print("g: " + str(float(u) * 1.66) + " * 10^-24")