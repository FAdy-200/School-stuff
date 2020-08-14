import numpy as np
import matplotlib.pyplot as plt


def load_points():
    y = np.load('cases.npy')
    x = np.array(range(1, len(y) + 1))
    return x, y


x, y = load_points()


def make(x, m):
    n = len(x)
    A = np.zeros((n, m + 1))
    A[:, 0] = 1
    for i in range(1, m + 1):
        A[:, i] = A[:, i - 1] * x
    return A


def final(A, y):
    At = A.transpose()
    a = np.linalg.solve(At.dot(A), At.dot(y))
    return a


plt.figure()
z = np.append(x, [i for i in range(x[-1] + 1, x[-1] + 8)])
plt.grid()
plt.scatter(x, y, color="m")
plt.axhline(y=0, color='k')
"""
i used the 3rd degree polynomial because the curve seems to fit the data the best without any over fitting as seen if we take the fourth order polynomial and 
no steep slopes are seen at the predicted data.
thus being the most applicable prediction. 

"""
g = 3
A = make(x, g)
a = final(A, y)
m = make(z, g)
ny = m.dot(a)
np.set_printoptions(linewidth=200)
print("number of cases in the predicted 7 days = \n", ny[-7:])
print(np.sum(ny))
plt.plot(z, ny)
plt.show()
