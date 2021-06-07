import math


def first_second_questions(a: str, b: str, f: bool) -> int:
    from math import inf
    # a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # b = "ABadfsafsaDasdasdEsdf"
    ag = [(0, 0)] * len(b)

    for i in range(len(b)):
        loc = []
        ma = []
        check = False
        for j in range(len(a)):
            if b[i] == a[j]:
                loc.append(j)
                ma.append(1)
                check = True
        if not check:
            # ag[i] = (inf, inf)
            continue
        for j in range(len(loc)):
            mma = [ma[j]]
            for k in range(i):
                if loc[j] > ag[k][1]:
                    mma.append(ag[k][0] + 1)
            ma[j] = max(mma)
        mm = max(ma)
        mmind = ma.index(mm)
        ag[i] = (mm, loc[mmind])
    mn = 0
    if not f:
        for j in ag:
            if j[0] > 0:
                mn = 1
    else:
        for j in ag:
            if j[0] > mn:
                mn = j[0]
    return mn


def new1A(x, y):
    if len(x) == 0:
        return True
    if len(y) == 0:
        return False
    if x[0] == y[0]:
        return True and new1A(x[1:], y[1:]) or new1A(x, y[1:])
    return new1A(x, y[1:])


def checkS(x, y, i):
    if len(y) == 0:
        return False
    if i == len(x):
        return True
    if x[i] == y[0]:
        return checkS(x, y[1:], i + 1) or checkS(x, y[1:], i)
    return checkS(x, y[1:], i)


def threeC(x, y, i1=0, i2=0):
    if len(y) == 0:
        return False
    if i1 == len(x):
        return checkS(x, y, i2)
    if i2 == len(x):
        return checkS(x, y, i1)
    if x[i1] == y[0] and x[i2] == y[0]:
        return threeC(x, y[1:], i1 + 1, i2) or threeC(x, y[1:], i1, i2 + 1) or threeC(x, y[1:], i1, i2)
    elif x[i1] == y[0]:
        return threeC(x, y[1:], i1 + 1, i2) or threeC(x, y[1:], i1, i2)
    elif x[i2] == y[0]:
        return threeC(x, y[1:], i1, i2 + 1) or threeC(x, y[1:], i1, i2)
    return threeC(x, y[1:], i1, i2)


def sec(x, y):
    if len(y) < len(x):
        return 0
    elif len(x) == 0:
        return len(y)
    if not checkS(x, y, 0):
        return 0
    if x[0] == y[0]:
        return min(1 + sec(x, y[1:]), sec(x[1:], y))
    return sec(x, y[1:])


def khara(a, b, i=0, j=0):
    if i == len(a) and j == len(b):
        return 0
    if i == len(a):
        return len(b) - j - 1
    if j == len(b):
        return len(a) - i - 1
    if a[i] == b[j]:
        return 1 + khara(a, b, i + 1, j + 1)
    else:
        return 1 + min(khara(a, b, i + 1, j + 1), khara(a, b, i, j + 1), khara(a, b, i + 1, j))


def sss(x, i, j):
    if i == len(x) - 1:
        return 0
    if x[j] > x[i] and j // 2 == 0:
        return max(1 + sss(x, i + 1, i), sss(x, i + 1, j))
    elif x[j] < x[i] and j // 2 != 0:
        return max(1 + sss(x, i + 1, i), sss(x, i + 1, j))
    return 0


def prod(x):
    mostNegative = x[0]
    mostPositive = x[0]
    current = x[0]
    for i in range(1, len(x)):
        if x[i] < 0:
            mostPositive, mostNegative = mostNegative, mostPositive
        mostPositive = max(x[i], mostPositive * x[i])
        mostNegative = min(x[i], mostNegative * x[i])
        current = max(current, mostNegative, mostPositive)
    return current


def summ(x):
    currentMax = -math.inf
    maxSoFar = 0
    for i in x:
        currentMax += i
        maxSoFar = max(currentMax, maxSoFar)
        currentMax = max(currentMax, 0)
    return maxSoFar


print(summ([-6, 12, -7, 0, 14, -7, 5]))
# print(sec("PPPPPPPP", "PENPINEAPPLEAPPLEPEN"))
# print(sec("aa", "aaaaa"))
# x = first_second_questions("PPPAP", "PRNPINEAPPLEAPPLEPEN", True)
# print(x)
# print(new1A("PPAP", "PRNPINEAPPLEPPLEPEN"))
# print(threeC("PPEP", "PENPINEAPPLEAPPLEPEN"))
# print(khara("ZZZ", "PENPINEAPPLEAPPLEPEN"))
# print(kk([0, 1, 0, 1, 0, 1, 0, 1, 0, 1], 9, 9))
# print(sss([0, 1, 0, 1, 0, 1], 0, 1))
# print(sec("PPZP", "PENPINEAPPLEAPPLEPEN"))
