import numpy as np
from prettytable import PrettyTable


def nev(x, y, u):
    n = len(x)
    ans = np.zeros((n, n))
    for j in range(n):
        for i in range(n - j):
            if j == 0:
                ans[i][0] = y[i]
            else:
                ans[i][j] = (ans[i][j - 1] * (u - x[i + j]) - ans[i + 1][j - 1] * (u - x[i])) / (x[i] - x[i + j])
    return ans


x = [1.0, 1.3, 1.6, 1.9, 2.2]
y = [0.7651977, 0.6200860, 0.4554022, 0.2818186, 0.1103623]
a = nev(x, y, 1.5)
table = PrettyTable()
table.header = False
for i in range(1,len(a)+1):
    z = [x[i - 1]]
    for k in a[-i]:
        z.append(k)
    table.add_row(z)
print(table)
print("answer = {}".format(a[0][len(a)-1]))

