import matplotlib.pyplot as plt
import numpy as np
import math


def f(x):
    # return 100 * x + np.log2(x) # both
    # return np.log2(x) # both
    # return (x ** 2) / np.log2(x) # lower
    # return (np.log2(x))**(np.log2(x)) # lower
    # return np.sqrt(x)  # lower
    # return x*(2**x) # upper
    # return 2**(np.sqrt(np.log2(x))) # lower
    # return x**2
    return x**(x**0.5)
    pass


def g(x):
    # return (x + (np.log2(x)) ** 2)*10000
    # return np.log2(x ** 2)
    # return x * ((np.log2(x)) ** 2)
    # return (x/(np.log2(x)))*1000000000000
    # return ((np.log2(x))**5)*10000000000000000000000000000
    # return 3**x
    # return np.sqrt(x)*0.01
    # return 2**x
    return 2**x
    pass


def plot():
    x = np.linspace(0.001,
                    1000,
                    100000)
    y1 = f(x)
    y2 = g(x)
    plt.figure()

    plt.plot(x, y1)
    plt.plot(x, y2)
    plt.legend(["f(n)", "g(n)"])
    plt.show()


# print(math.log(1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000,4))
# print(math.log2(math.log2(1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)))
# plot()
print(f(27))
print(g(27))