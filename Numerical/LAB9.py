"""
###############################################################################
#=============================  Numerical Analysis ===========================#
#=============================        LAB 9        ===========================#
#=============================    3 / 5 / 2020    ===========================#
###############################################################################

In this lab, you are going to implement Jacobi and Gauss-Seidel methods
###############################################################################
"""

import numpy as np
from numpy.linalg import inv


def jacobi(A, b, N):
    x = np.zeros_like(b)
    k = np.zeros((len(x), N + 1))
    d = np.diag(A)
    D = np.diag(d)
    A = A - D
    for i in range(N):
        x = np.diag((b - A @ x) / d)
        k[:, i + 1] = x.T
    return k


def seidel(A, b, N):
    '''
    return array S where column k represents c4t at iteration k
    '''
    D = np.diag(np.diag(A))
    L = np.tril(A)
    U = np.triu(A) - D
    x = np.zeros_like(b)
    S = np.zeros((len(b), N + 1))
    for i in range(N):
        x = inv(L) @ (b - U @ x)
        S[:, i + 1] = x.T

    return S


if __name__ == '__main__':
    np.random.seed(42)
    A = 10 * np.eye(10)
    A = A + np.random.rand(10, 10)
    b = np.sum(A, axis=1)
    b = b.reshape(len(b), 1)
    np.set_printoptions(linewidth=10000000)
    print(seidel(A, b, 12))
    print(jacobi(A, b, 12))









































