import numpy as np
def fcm(x):
    return x**3-3*x**2+2*x
def trapsum ( fcn , a , b , N) :
    """
    Function for approximating the integral of
    the function ‘ fcn ‘ over the interval [a, b]
    in N segments using the trapezoid rule.
    """
    h=(b-a)/N
    s=(fcn(a)+fcn(b)) /2
    for k in range (1 , N) :
        s+=fcn(a+k*h)
    return s * h
    #
for k in range (8) :
    N=2**k
    I=trapsum(fcm, 0, 3, N)
    print (N, I)