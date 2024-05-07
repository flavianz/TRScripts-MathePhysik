import math


def is_empty(string):
    return string == "" or string == " "


a = input("a: ")
b = input("b: ")
c = input("c: ")
alpha = input("alpha: ")
beta = input("beta: ")
gamma = input("gamma: ")


def sin_satz_seite(zaehler, nenner, winkel):
    return str(zaehler / math.sin(math.radians(nenner)) * math.sin(math.radians(winkel)))


def find_side(side, opposite_angle, otherside1, otherangle1, otherside2, otherangle2):
    if is_empty(side):
        if not is_empty(opposite_angle):
            # Sinussatz
            if not is_empty(otherside1) and not is_empty(otherangle1):
                return sin_satz_seite(float(otherside1), float(otherangle1), float(opposite_angle))
            elif not is_empty(otherside2) and not is_empty(otherangle2):
                return sin_satz_seite(float(otherside2), float(otherangle2), float(opposite_angle))
            # Cosinussatz
            elif not is_empty(otherside1) and not is_empty(otherside2):
                return str(math.sqrt(
                    float(otherside1) ** 2 + float(otherside2) ** 2 - 2 * float(otherside1) * float(
                        otherside2) * math.cos(
                        math.radians(float(opposite_angle)))))
            else:
                return ""
        else:
            return ""
    else:
        return side


def find_angle(angle, opposite_side, otherside1, otherangle1, otherside2, otherangle2):
    if is_empty(angle):
        # Winkelauffüllen
        if not is_empty(otherangle1) and not is_empty(otherangle2):
            return str(180 - float(otherangle1) - float(otherangle2))
        # Cosinussatz
        elif (not is_empty(opposite_side) and not is_empty(otherside1)
              and not is_empty(otherside2)):
            return str(math.degrees(math.acos(math.radians(float(
                opposite_side) ** 2 / (float(otherside1) ** 2 + float(
                otherside2) ** 2 - 2 * float(otherside1) * float(otherside2))))))
        # Sinussätze
        elif not is_empty(opposite_side):
            if not is_empty(otherside1) and not is_empty(otherangle1):
                return str(math.degrees(math.asin(math.sin(math.radians(
                    float(otherangle1))) / float(otherside1) * float(opposite_side))))
            elif not is_empty(otherside2) and not is_empty(otherangle2):
                return str(math.degrees(math.asin(math.sin(math.radians(
                    float(otherangle2))) / float(otherside2) * float(opposite_side))))
            else:
                return ""
        else:
            return ""
    else:
        return angle


a = find_side(a, alpha, b, beta, c, gamma)
b = find_side(b, beta, a, alpha, c, gamma)
c = find_side(c, gamma, a, alpha, b, beta)

print("\na: " + a + "\nb: " + b + "\nc: " + c + "\nalpha: " + alpha + "\nbeta: " + beta + "\ngamma: " + gamma)
