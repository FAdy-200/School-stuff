import numpy as np


def re(a, x, i, j):
    if j == 0:
        return a[i][1]
    else:
        k = (re(a, x, i, j - 1) * (x - a[i - j][0]) - re(a, x, i - 1, j - 1) * (x - a[i][0])) / (a[i][0] - a[i - j][0])
        a[i][j + 1] = k
        return k


u = [8.1, 8.3, 8.6, 8.7]
y = [16.94410, 17.56492, 18.50515, 18.82091]
ans = np.zeros((len(u), len(u) + 1))
for _ in range(len(u)):
    ans[_][0] = u[_]
    ans[_][1] = y[_]
re(ans, 8.4, len(u) - 1, len(u) - 1)
f_ans = (ans[len(u) - 1][len(u)])
try:
    from prettytable import PrettyTable

    table = PrettyTable()
    o = ["X"]
    for m in range(len(u)):
        table.add_row(ans[m])
        o.append("Degree {}".format(m))
    table.field_names = o
    print(table)
except:
    print(ans)
print("the final answer is %.53f" % f_ans)
