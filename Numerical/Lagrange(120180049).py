import numpy as np
import matplotlib.pyplot as plt
import time
import sympy as sy

st = time.time()

u = sy.symbols("c4t")


def f(y):
    return 1 / (1 + 25 * y ** 2)


def Ll(x, y, u):
    return sum([y[i] * np.product([((u - j) / (x[i] - j)) for j in x if j != x[i]]) for i in range(len(x))])


# c4t = [-1,-0.5,0,0.5,1]
# y = [f(i) for i in c4t]
# c4t = [0, 1, 2, 3]
# y = [1, 3, 5, 7]
# print(sy.expand(Ll(c4t, y, u)))


# -------solving the equation------

# def L(c4t, i, y):
#     return np.product([((y - j) / (c4t[i] - j)) for j in c4t if j != c4t[i]])


def lag(x, y, a, b):
    # so = [sum([y[i] * np.product([((p - j) / (c4t[i] - j)) for j in c4t if j != c4t[i]]) for i in range(len(c4t))]) for p in [k / 100 for k in range(a * 100, b * 100 + 1)]]
    plt.plot([k / 100 for k in range(a * 100, b * 100 + 1)],
             [sum([y[i] * np.product([((p - j) / (x[i] - j)) for j in x if j != x[i]]) for i in range(len(x))]) for p in
              [k / 100 for k in range(a * 100, b * 100 + 1)]])


# ----------------------potting-------
# -------------function 1
x1 = np.arange(0, 1, 0.01)
z1 = [0, 0.5, 1]
y1 = [f(i) for i in z1]
lag(z1, y1, 0, 1)
plt.plot(x1, f(x1))
plt.axhline(y=0, color='k')
plt.axvline(x=0, color="k")
plt.show()
# -----------function 2
# x2 = np.arange(-1, 0, 0.01)
# z2 = [-1, -0.5, 0]
# y2 = [f(i) for i in z2]
# lag(z2, y2, -1, 0)
# plt.plot(x2, f(x2))
# plt.axhline(y=0, color='k')
# plt.axvline(c4t=0, color="k")
# plt.show()
# print(time.time()-st)
