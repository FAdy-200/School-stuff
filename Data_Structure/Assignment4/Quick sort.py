import time


def quick(x):
    le = len(x)
    if le < 2:
        return x
    l = 0
    r = le - 1
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


def quickR(x, l=None, r=None):
    if l is None and r is None:
        l = 0
        r = len(x) - 1
    if l >= r and l is not None:
        return

    p = (l + r) // 2
    lc = rc = False
    lo = l
    ro = r
    po = x[p]
    pp = p
    print(x, ",p =", po, ",l =", lo, ",r =", ro)
    print(x[lo:ro + 1], "the important part of the array on which the algorithm is working")
    while l <= r:
        while x[l] < po:
            l += 1
        while x[r] > po:
            r -= 1
        if l <= r:
            print("swapping arr[{}], arr[{}]".format(l, r))
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
            print("array after swapping =", x[lo:ro + 1], ",l =", l, ",r =", r)
    if pp != p and lc:
        print("swapping arr[{}], arr[{}]".format(l, pp))
        x[pp], x[l] = x[l], x[pp]
        print("array after swapping =", x[lo:ro + 1], ",l =", l, ",r =", r)
    elif pp != p and rc:
        print("swapping arr[{}], arr[{}]".format(pp, r))
        x[pp], x[r] = x[r], x[pp]
        print("array after swapping =", x[lo:ro + 1], ",l =", l, ",r =", r)
    if rc:
        print(x)
        print()
        quickR(x, r + 1, ro)
        quickR(x, lo, r - 1)
    else:
        print(x, "full array after modification")
        print()
        quickR(x, l + 1, ro)
        quickR(x, lo, l - 1)


def quickLecture(x, l=None, r=None, xo=False):
    if l is None and r is None:
        l = 0
        r = len(x) - 1
    if l >= r and l is not None:
        return
    xs = list(sorted(x[l:r + 1]))

    p = (l + r) // 2
    lo = l
    ro = r
    po = x[p]
    print("Pivot Location in subarray =", p - l)
    print("subarray =", x[lo:ro + 1])
    while l <= r:
        while x[l] < po:
            l += 1
        while x[r] > po:
            r -= 1
        if l <= r:
            x[r], x[l] = x[l], x[r]
            l += 1
            r -= 1
    print("The arrangement of the numbers =", x)
    print()
    if xs == x[lo:ro + 1] and xo:
        return
    if xs == x[lo:ro + 1]:
        quickR(x, l, ro, True)
        quickR(x, lo, l - 1, True)
    else:
        quickR(x, l, ro)
        quickR(x, lo, l - 1)
    # else:
    #     print(x, "full array after modification")
    #     print()
    #     quickR(x, l + 1, ro)
    #     quickR(x, lo, l - 1)


# <editor-fold desc="Description">
# x = [8, 1, 4, 1, 5, 9, 2, 6, 5]
# # x = [12] * 1000000
# z = x[:]
# y = quick(x)
# t1 = time.time()
# # print(time.time() - t1)
# # print(y)
# t2 = time.time()
# quickR(z)
# # print(time.time() - t2)
# # print(z, " Final result")
# </editor-fold>
x = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print(60-sum(x))
