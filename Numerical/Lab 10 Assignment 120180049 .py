from prettytable import PrettyTable
import matplotlib.pyplot as plt


def df(x, y):
    r = []
    o = []
    fo = []

    for i in range(len(x)):
        if i == 0:
            f = "Forward Finite Difference"
            h = abs(x[i] - x[i + 1])
            d = (y[i + 1] - y[i]) / abs(x[i] - x[i + 1])
        elif i == len(x) - 1:
            f = "Backward Finite Difference"
            h = abs(x[i] - x[i - 1])
            d = (y[i] - y[i - 1]) / abs(x[i] - x[i - 1])
        else:
            try:
                m = 1
                while m < len(x[i:])+1:
                    for k in range(1, len(x[:i]) + 1):
                        if abs(x[i + m] - x[i]) == abs(x[i - k] - x[i]):
                            f = "Three point mid point"
                            h = abs(x[i + m] - x[i])
                            d = (y[i + m] - y[i - k]) / abs(x[i + m] - x[i - k])
                            m = len(x[i:]) + 2
                            break
                    m += 1
            except:
                print("point in position {} can't be differentiated using the Three point mid point formula".format(i))
                print('Forward Finite Difference formula will be used')
                f = "Forward Finite Difference"
                h = abs(x[i] - x[i - 1])
                d = (y[i] - y[i - 1]) / abs(x[i] - x[i - 1])
        o.append(h)
        r.append(d)
        fo.append(f)
    return r, o, fo


x = [0, 2, 4, 6, 8, 10, 12, 14, 16, 20]
y = [8.23, 9.66, 10.95, 12.68, 14.20, 15.5, 16.27, 18.78, 22.27, 24.56]
rate = df(x, y)

table = PrettyTable()
table.add_column('Day ', x)
table.add_column('Height in Inches', y)
table.add_column("h", rate[1])
table.add_column('Formula used', rate[2])
table.add_column('Rate of growth', rate[0])
print(table)

plt.figure()
plt.grid()
plt.plot(x, rate[0], color="r")
plt.legend(['Rate of Growth'])
plt.show()

