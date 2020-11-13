class node():
    def __init__(self, val):
        self.val = val
        self.nv = None


class ll():
    def __init__(self):
        self.head = None
        self.numberOfValues = 0

    def addStart(self, val):
        val.nv = self.head
        self.head = val
        self.numberOfValues += 1

    def addLast(self, val):
        n = self.head
        while n.nv is not None:
            n = n.nv
        n.nv = val
        self.numberOfValues += 1


l = ll()
l.addStart(node(1))
l.addLast(node(5))
l.addLast(node(6))
l.addLast(node(7))
l.addLast(node(8))


def r(l):
    c = l.head.nv
    t2 = c.nv
    c.nv = None
    t1 = c
    c = t2
    t2 = t2.nv
    while t2 is not None:
        c.nv = t1
        t1 = c
        c = t2
        t2 = t2.nv
    c.nv = t1
    temp = l.head
    l.head = c
    return l, temp


r(l)


def groupR(list, k):
    j = 0
    c = list.head
    while j < list.numberOfValues:
        midl = ll()
        for i in range(k):
            midl.addLast(c)
            try:
                c = c.nv
            except:
                break
        midl = r(midl)


c = l.head
while c is not None:
    print(c.val)
    c = c.nv
