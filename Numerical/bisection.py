import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable
# --------potting-------
x = np.arange(0, 2.5, 0.01)
plt.figure()
plt.plot(x, (np.exp(x) - 5 * x + 2), color="purple")
plt.axhline(y=0, color='grey')

# -------solving the equation------
gg = []


def f(m):
    return np.exp(m) - 5 * m + 2


def bi(a, b, e):
    p = (a + b) / 2
    while abs(b - a) > 2 * e:
        po = p
        p = (a + b) / 2
        if f(p) * f(a) > 0:
            a = p
        else:
            b = p
        plt.scatter(p, f(p), color="green", s=50)
        gg.append([a, b, f(a), f(p), p, po])
    return p


# ------plotting the solutions------
sol = bi(0.1, 1, 1e-5)
plt.scatter(sol, f(sol), color="red", s=50)

# ------printing the steps and showing the graph--------
table = PrettyTable()
table.field_names = ['It#', "a", "b", "f(a)", "f(p)", "abs(pn-pn_-1)/pn"]
o = 1
for i in gg:
    table.add_row([o, i[0], i[1], i[2], i[3], abs(i[4] - i[5]) / i[4]])
    o += 1
print(table)
print('Final solution =', sol)
plt.show()