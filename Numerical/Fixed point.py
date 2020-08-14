import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable
x = np.arange(1, 2, 0.01)


def f(y):
    return np.sqrt((10 - y ** 3) / 4)


# --------potting-------
plt.figure()
plt.plot(x, f(x), color="C1")
plt.plot(x, x, color="m")
plt.axhline(y=0, color='k')

plt.grid()
# -------solving the equation------


gg = []


def fix(a, b, e):
    xo = a
    xn = f(xo)
    while abs(xn - xo) >= e:
        gg.append([xn, xo, f(xn), f(xo)])
        plt.scatter(xn, f(xn), color="green", s=20)
        plt.axvline(xn, ls="--", color="g")
        xo = xn
        xn = f(xo)

    return xn


sol = fix(1, 2, 1e-5)
# ------plotting the solutions------
plt.scatter(sol, f(sol), color="red", s=20)
plt.axvline(sol, ls="--", color="m")

table = PrettyTable()
table.field_names = ["It#", "X_n", "X_n-1", "f(X_n)", "f(X_n-1)", "abs(Xn-Xn_-1)/Xn"]
o = 1
for i in gg:
    table.add_row([o, i[0], i[1], i[2], i[3], abs(i[0] - i[1]) / i[0]])
    o += 1
print(table)
print('Final solution =%.20f' % sol)

plt.show()
