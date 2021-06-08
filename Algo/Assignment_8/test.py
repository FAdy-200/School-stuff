from math import inf


def kPalindrome(x):
    mn = inf
    j = 0
    i = 1
    lasti = -1
    while i < len(x):
        if x[i] == x[j]:
            while i < len(x) and j >= 0:
                i += 1
                j -= 1
                if i == len(x) or j < 0:
                    i -= 1
                    j += 1
                    mn = min(mn, i - j + 1)
                    if j != lasti + 1:
                        mn = 1
                    lasti = i
                    j = i + 1
                    i += 2
                    break
                if x[i] != x[j]:
                    mn = min(mn, i - j - 1)
                    if j != lasti + 1:
                        mn = 1
                    lasti = j
                    j = i + 1
                    i += 2
                    break
        else:
            i += 1
            j += 1
    if mn < inf and j == lasti + 1:
        return mn
    return 1


z = kPalindrome("idFssFdijhj")
print(z)
