import numpy as np
import matplotlib.pyplot as plt
from random import random


def f(x):
    a = random()
    j = np.cos(2 * np.pi * x) + a
    return j


def make(x, m):
    n = x.shape[0]
    ans = np.zeros((n, m + 1))
    ans[:, 0] = 1
    for i in range(1, m + 1):
        ans[:, i] = ans[:, i - 1] * x
    return ans


def final(a, y):
    at = a.transpose()
    k = np.linalg.solve(at.dot(a), at.dot(y))
    return k


plt.figure()
# x = np.arange(0, 1.01, 0.01)
x = np.linspace(0, 1, 101, endpoint=True)
# print(z)
y = f(x)
# print(x,y)
plt.scatter(x, y)
g = int(input())
for i in range(g + 1):
    A = make(x, i)
    a = final(A, y)
    plt.plot(x, A.dot(a))
plt.legend(list(range(g + 1)))
plt.show()
