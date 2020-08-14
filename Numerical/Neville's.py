import numpy as np
import sympy

import time

st = time.time()


def re(x, y, u, i, j):
    global ans

    if j == 0:
        return y[i]
    else:
        k = (re(x, y, u, i, j - 1) * (u - x[i - j]) - re(x, y, u, i - 1, j - 1) * (u - x[i])) / (x[i] - x[i - j])
        ans[i][j] = k
        return k


def a1d(x, y, u):
    n = len(x)
    q = y[:]
    for k in range(1, n):
        for i in range(n - k):
            q[i] = (-q[i] * (u - x[i + k]) + q[i + 1] * (u - x[i])) / (x[i + k] - x[i])

    return "%.50f" % q[0]


def a2d(x, y, u):
    n = len(x)
    ans = np.zeros((n, n))
    for j in range(n):
        for i in range(n - j):
            if j == 0:
                ans[i][0] = y[i]
            else:
                ans[i][j] = (ans[i][j - 1] * (u - x[i + j]) - ans[i + 1][j - 1] * (u - x[i])) / (x[i] - x[i + j])
    return ans


x1 = [np.float128(1), np.float128(2), np.float128(3), np.float128(4), np.float128(6)]
y1 = [np.exp(i) for i in x1]
ans = np.zeros((len(x1), len(x1)))
# s_a1d = a1d(x1, y1, 1.5)
# s_a2d = a2d(x1, y1, 1.5)
s_re = re(x1, y1, 1.5, len(x1) - 1, len(x1) - 1)
# print(s_a1d)
# print(s_a2d)
print(ans)
# print(st - time.time())
