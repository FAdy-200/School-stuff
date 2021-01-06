def quick(x):
    if len(x) < 2:
        return x
    l = 0
    r = len(x) - 1
    p = (l + r) // 2
    lc = rc = False
    po = x[p]
    pp = p
    while l <= r:
        while x[l] < po:
            l += 1
        while x[r] > po:
            r -= 1
        if l <= r:
            x[r], x[l] = x[l], x[r]
            if x[p] != po:
                if x[r] == po:
                    pp = r
                    lc = True
                else:
                    pp = l
                    rc = True
            l += 1
            r -= 1
    if pp != p and lc:
        x[pp], x[l] = x[l], x[pp]
    elif pp != p and rc:
        x[pp], x[r] = x[r], x[pp]
    if rc:
        y = quick(x[:r]) + [x[r]] + quick(x[r + 1:])
    else:
        y = quick(x[:l]) + [x[l]] + quick(x[l + 1:])
    return y


def quickR(x, l, r):
    if l >= r:
        return
    p = (l + r) // 2
    lc = rc = False
    lo = l
    ro = r
    po = x[p]
    pp = p
    print(x, "p=", po, "l=", lo, "r=", ro)
    print(x[lo:ro + 1]," array part the algorithm is working on")
    while l <= r:
        while x[l] < po:
            l += 1
        while x[r] > po:
            r -= 1
        if l <= r:
            x[r], x[l] = x[l], x[r]
            if x[p] != po:
                if x[r] == po:
                    pp = r
                    lc = True
                else:
                    pp = l
                    rc = True
            l += 1
            r -= 1
    if pp != p and lc:
        x[pp], x[l] = x[l], x[pp]
    elif pp != p and rc:
        x[pp], x[r] = x[r], x[pp]
    if rc:
        print(x)
        print()
        quickR(x, r + 1, ro)
        quickR(x, lo, r - 1)
    else:
        print(x," array after modification")
        print()
        quickR(x, l + 1, ro)
        quickR(x, lo, l - 1)


x = [8, 1, 4, 1, 5, 9, 2, 6, 5]
z = x[:]
y = quick(x)
# print(y)
quickR(z, 0, 8)
print(z," Final result")
