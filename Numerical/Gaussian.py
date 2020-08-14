import numpy as np


def Ninp():
    n = int(input())
    x = []
    for _ in range(n):
        x.append(list(map(float, input().split())))
    z = np.array(x)
    return z


def Iinp():
    n = int(input())
    x = []
    y = np.identity(n)
    for _ in range(n):
        x.append(list(map(float, input().split())))
    z = np.array(x)
    z = np.hstack((z, y))
    return z, n


def gauss(A):
    a = np.copy(A)
    k = True
    for i in range(a.shape[0]):
        try:
            if a[i, i] == 0:
                for l in range(1, a.shape[0] - i + 1):
                    if a[i, i] == 0:
                        t = np.copy(a[i])
                        a[i] = np.copy(a[i + l])
                        a[i + l] = np.copy(t)
        except:
            k = False
            break
        for j in range(a.shape[0]):
            if j == i:
                pass
            else:
                a[j] = a[j] - a[i] * (a[j, i] / a[i, i])
        if a[i, i] != 1:
            a[i] = a[i] / a[i, i]
    if k:
        return a
    else:
        return 'there is no solution'


def hilbert(n):
    h = np.fromfunction(lambda i, j: 1 / (i + j + 1), (n, n), dtype=np.float64)
    b = np.sum(h, axis=1)
    z = np.hstack((h, b[:, None]))
    return z


def cond(a):
    ad = np.linalg.norm(a)
    adn = np.linalg.norm(np.linalg.inv(a))
    return ad * adn


np.set_printoptions(linewidth=100000)
A = Ninp()
# ans = gauss(A[0])
# print(A[0][:,:A[1]])
# inv = ans[:, -A[1]:]
# print(inv)
# print(np.linalg.inv(A[0][:, :A[1]]))
# print(np.linalg.inv(A[0][:, :A[1]]) @ A[0][:, :A[1]])
# print(A[0][:, :A[1]] @ inv)
# for i in range(len(ans)):
#     print('x_%.0f = %.4f' % (i, ans[i]))


# ------------test cases

# 4
# 1 1 0 3 4
# 2 1 -1 1 1
# 3 -1 -1 2 -3
# -1 2 3 -1 4

# 4
# 1 1 0 3
# 2 1 -1 1
# 3 -1 -1 2
# -1 2 3 -1

# 3
# 3 0 2
# 2 0 -2
# 0 1 1
