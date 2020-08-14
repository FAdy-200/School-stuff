import numpy as np


def inv(A):
    a = np.copy(A)
    n = a.shape[0]
    I = np.identity(n)
    a = np.hstack((a, I))
    for i in range(a.shape[0]):
        # ---checking if the pivot element is zero and changing the row if necessary
        if a[i, i] == 0:
            k = np.where(abs(a[i + 1:, i]) == max(abs(a[i + 1:, i])))
            a[i], a[i + k[0] + 1] = np.copy(a[i + k[0] + 1]), np.copy(a[i])
        # ---doing the operation on the entire column of the pivot not just the elements under it thus obtaining the reduced echelon form
        for j in range(a.shape[0]):
            if j != i:
                a[j] = a[j] - a[i] * (a[j, i] / a[i, i])
        # ----checking if the pivot is 1 if not make it
        if a[i, i] != 1:
            a[i] = a[i] / a[i, i]
    return a[:, n:]



