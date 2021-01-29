from prettytable import PrettyTable
import matplotlib.pyplot as plt


def df_approx(y, x, index):
    return (y[index] - y[index - 1]) / (x[index] - x[index - 1])


def df_midpoint_approx(y, x, index):
    return (y[index + 1] - y[index - 1]) / (2 * (x[index] - x[index - 1]))


x = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
y = [8.23, 9.66, 10.95, 12.68, 14.20, 15.5, 16.27, 18.78, 22.27, 24.56]
r = []
for i in range(len(y)):
    if i == 0:
        rate = df_approx(y, x, i + 1)
    elif i == len(y) - 1:
        rate = df_approx(y, x, i)
    else:
        rate = df_midpoint_approx(y, x, i)
    r.append(rate)

table = PrettyTable()
table.add_column('c4t', x)
table.add_column('y', y)
table.add_column('rate of growth', r)
print(table)

plt.figure()
plt.plot(x, r)
plt.grid()
plt.show()
