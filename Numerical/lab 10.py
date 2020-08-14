"""
###############################################################################
#=============================  Numerical Analysis ===========================#
#=============================       LAB 10        ===========================#
#=============================    10 / 5 / 2020    ===========================#
###############################################################################

In this lab, you are going to implement differentiation approximation algorith-
ms.

###############################################################################
"""

import numpy as np
import math
from prettytable import PrettyTable


def df_approx(f, x0, h):
    """
    Forward pass difference formula
    returns f'(x) for x = x0
    """
    return (np.cos(x0 + h) - np.cos(x0)) / h


def df_midpoint_approx(f, x0, h):
    '''
    Three point mid-point formula
    returns f'(x) for x = x0
    '''
    return (np.cos(x0 + h) - np.cos(x0 - h)) / (2 * h)


if __name__ == '__main__':
    x = 0.7
    k = 30
    h = [2 ** (-i) for i in range(k)]



    def f(y):
        return np.cos(y)


    values = []
    ks = []
    ab = []
    rae = [np.NAN]
    rx = -np.sin(x)
    for i in h:
        a = df_midpoint_approx(np.cos, x, i)
        values.append(a)
        ks.append(h.index(i)+1)
        ab.append(abs(rx-a))
    for i in range(0, 29):
        rae.append(ab[i]/ab[i+1])
    table = PrettyTable()
    table.add_column("k", ks)
    table.add_column("f'(x)", values)
    table.add_column("Absolute error", ab)
    table.add_column("Ratio of error", rae)
    print(table)




