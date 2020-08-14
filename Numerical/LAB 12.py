"""
###############################################################################
#=============================  Numerical Analysis ===========================#
#=============================       LAB 12        ===========================#
#=============================    7  / 6 / 2020    ===========================#
###############################################################################

In this lab, you are going to implement Euler's Method for ODE IVP.

###############################################################################
"""
import numpy as np
from prettytable import PrettyTable
import matplotlib.pylab as plt


def euler(f, a, b, y0, N):
    '''
    Implementation of Euler method. The inputs required are the function f,
    the interval [a, b] over which the solution is sought, the initial value
    y0= y(a) , and the number of steps to be used.
    The output here consists of a table of values xk, yk.
    '''
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

    return (xk, yk)


# gg = euler(f, 0, 1, 1, 4)
# xk = list(gg.keys())
# yk = list(gg.values())
# table = PrettyTable()
# table.add_column('k',[i for i in range(4+1)])
# table.add_column('x',xk)
# table.add_column('y',yk)
# print(table)


def f(x, y):
    return (1/(x**2))-(y/x)-y**2

def rf(x):
    return -1/x


if __name__ == "__main__":
    '''
    Applying the program to the solution of the initial value problem 
    y = (6*x**2 - 1)*y ; y(0)= 1 in the interval [0, 1]. Assume N = 4.
    '''
    gg = euler(f, 1, 2, -1, int(1/0.05))
    r = [rf(i) for i in (gg[0])]
    table = PrettyTable()
    table.add_column('i', [i for i in range(int(1/0.05) + 1)])
    table.add_column('t', gg[0])
    table.add_column('w', gg[1])
    table.add_column('y', r)
    table.add_column('|w-y|',[abs(r[i]-gg[1][i]) for i in range(len(r))])

    print(table)

    '''
    Repeat the previous problem but begin with N = 4 steps and repeatedly 
    double this number of steps up to 256. Report the final y value and
    the error given that the actual solution y(x) = exp(2*x**3 - x) and
    y(1) = e.
    '''
    # i = 4
    # il = [4]
    # error = []
    # error_ratio = []
    # yl = []
    # while i <= 128:
    #     k = euler(f, 0, 1, 1, i)
    #     error.append(abs(np.exp(1)-k[1][-1]))
    #     yl.append(k[1][-1])
    #     if i != 4:
    #         error_ratio.append(error[-1]/error[-2])
    #     i *= 2
    #     il.append(i)
    # error_ratio.append(np.NAN)
    #
    # table = PrettyTable()
    # table.add_column('N',il[:-1])
    # table.add_column('y',np.array(yl))
    # table.add_column('Error',np.array(error))
    # table.add_column('Error ratio', error_ratio)
    # print(table)
    # plt.Figure()
    # plt.plot(il[:-1], yl)
    # plt.axhline(y=np.exp(1), color='r')
    # plt.show()

    '''
    Report the error ratio (Error_N+1 / Error_N) for N = 4, 8, 16, ... , 256
    '''
    '''
    Plot the obtained solutions for each value of N.
    '''

