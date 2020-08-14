import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable

x = np.arange(4, 7, 0.01)


def f(y):
    return np.sin(y + 3) + 8 - 2 * y


# --------potting-------
plt.figure()
plt.plot(x, f(x))
plt.axhline(y=0, color='k')


# -------solving the equation------

def df(y):
    return -2 + np.cos(y + 3)


def df2(y):
    return -np.sin(y + 3)


gg = []


def newton(a, b, e):
    xo = a
    xn = xo - f(xo) / df(xo)
    while abs(xn - xo) >= e:
        gg.append([xn, xo, f(xn), f(xo)])
        plt.scatter(xn, f(xn), color="green", s=20)
        plt.axvline(xn, ls="--", color="g")
        xo = xn
        xn = xo - f(xo) / df(xo)
    return xn


def newtonadv(a, b, e):
    xo = a
    xn = xo - (f(xo) * df(xo)) / ((df(xo) ** 2) - f(xo) * df2(xo))
    while abs(xn - xo) >= e:
        gg.append([xn, xo, f(xn), f(xo)])
        plt.scatter(xn, f(xn), color="green", s=20)
        plt.axvline(xn, ls="--", color="g")
        xo = xn
        xn = xo - (f(xo) * df(xo)) / ((df(xo) ** 2) - f(xo) * df2(xo))
    return xn


sol = newton(4, 7, 1e-3)
# ------plotting the solutions------

plt.scatter(sol, f(sol), color="red", s=20)
plt.axvline(sol, ls="--", color="m")

table = PrettyTable()
table.field_names = ["It#", "X_n", "X_n-1", "f(X_n)", "f(X_n-1)",
                     'abs(Xn-Xn_-1)',
                     "abs(Xn-Xn_-1)/Xn"]
o = 1
for i in gg:
    table.add_row([o, i[0], i[1], i[2], i[3], abs(i[0] - i[1]), abs(i[0] - i[1]) / i[0]])
    o += 1
print(table)
print('Final solution =%.20f' % sol)
print('Number of iterations taken = {}'.format(o - 1))
plt.show()
