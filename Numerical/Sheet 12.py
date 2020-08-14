from prettytable import PrettyTable


def euler(f, a, b, y0, N):
    h = (b - a) / N
    t = a
    w = y0
    xk = [a]
    yk = [y0]
    for i in range(1, N + 1):
        w = w + h * f(t, w)
        t = a + i * h
        xk.append(t)
        yk.append(w)

    return xk, yk


def f(x, y):
    return (1 / (x ** 2)) - (y / x) - y ** 2


def rf(x):
    return -1 / x


gg = euler(f, 1, 2, -1, int(1 / 0.05))
r = [rf(i) for i in (gg[0])]
table = PrettyTable()
table.add_column('i', [i for i in range(int(1 / 0.05) + 1)])
table.add_column('t', gg[0])
table.add_column('w', gg[1])
table.add_column('y', r)
table.add_column('|w-y|', [abs(r[i] - gg[1][i]) for i in range(len(r))])

print(table)
