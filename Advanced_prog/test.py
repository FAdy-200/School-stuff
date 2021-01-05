class A:
    i = 0

    def __init__(self, i=i):
        self.i = i


class B(A):
    def __init__(self, j=1):
        self.j = j


b = B()
print(b.i)
print(b.j)


class a:
    def __i(self):
        print("a")

    def pr(self):
        self.__i()


class b(a):
    def __i(self):
        print("a")


A = a()
B = b()
A.pr()
B.pr()
