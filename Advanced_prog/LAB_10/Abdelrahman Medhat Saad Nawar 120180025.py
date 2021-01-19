# CSE314- Lab 9
#
# Topic: Functional Programming
# Author : Abdelrahman Medhat Saad Nawar 120180025
# Date : 12/01/2021
# Question 1:

"""
comprehension[0]
Lambs
comprehension[2]
Orangutans
"""

# Question 2:

text_arr = ['Abdelrahman', 'Medhat', 'Saad', 'Nawar']
text_arr_new = list(filter(lambda x: len(x) > 4, text_arr))

# Question 3:

A = [i for i in range(1, 51)]
B = list(sorted(A, key=lambda x: x % 2))

# Question 4:

Q = [(i, j) for i in range(1, 11) for j in range(i + 1, 11) if i % 2 != 0 and j % 2 != 0]

# Question 5:

a = lambda: 2
b = lambda x: 1
c = lambda x: x
d = lambda x, y: x + y
e = lambda x, y: max(x, y)
f = lambda x, y: int(str(y) + str(x))
g = lambda x: lambda y: int(str(x) + str(y))
h = lambda: lambda x: x + 5
i = lambda x, y: lambda z: x + z
j = lambda x: lambda y: x(y)
k = lambda x: x + 1
m = lambda x: 5
n = lambda: 5
o = lambda x: x
p = lambda x, y: lambda z: x(y(z))
q = lambda x: lambda y: y + " " + x
r = lambda x, y: (x // 2) + y() * 1000
s = lambda f0: f0(lambda: lambda f1: f1)


def t(x):
    return lambda y: "arc" + x + y


def u(x):
    return t("co")(x)


def v():
    return u("secant")
