from prettytable import PrettyTable
import matplotlib.pyplot as plt


def df_approx_backward(y, x, i):
    return (y[i] - y[i - 1]) / (x[i] - x[i - 1])


def df_approx_forward(y, x, i):
    return (y[i + 1] - y[i]) / (x[i + 1] - x[i])


def df_midpoint_approx(y, x, i):
    j = 1
    while j < len(x):
        for k in range(1, len(x)):
            if abs(x[i + j] - x[i]) == abs(x[i - k] - x[i]):
                d = (y[i + j] - y[i - k]) / (2 * (x[i] - x[i - k]))
                j = len(x)
                break
        j += 1
    return d


x = [0, 2, 4, 6, 8, 10, 12, 14, 16, 20]
y = [8.23, 9.66, 10.95, 12.68, 14.20, 15.5, 16.27, 18.78, 22.27, 24.56]
rate = []

for i in range(10):
    if i == 0:
        df = df_approx_forward(y, x, i)
    elif i == len(y) - 1:
        df = df_approx_backward(y, x, i)
    else:
        df = df_midpoint_approx(y, x, i)
    rate.append(df)

table = PrettyTable()
table.add_column('x', x)
table.add_column('y', y)
table.add_column('rate of growth', rate)
print(table)
plt.figure()
plt.plot(x, rate)
plt.grid()
plt.show()
