class node():
    def __init__(self, val):
        self.val = val
        self.nv = None




class ll():
    def __init__(self):
        self.head = None
        self.numberOfValues = 0
    def addStart(self,val):
        val.nv=self.head
        self.head = val
    def addLast(self,val):
        n = self.head
        while n.nv is not None:
            n = n.nv
        n.nv = val



l = ll()
l.addStart(node(1))
l.addLast(node(5))
l.addLast(node(6))
l.addLast(node(7))
l.addLast(node(8))


def r(l,k):
    c = l.head
    t = c.nv
    ft = l.head
    zz = 1
    while zz is not None:
        for i in range(1, k):
            j = t.val
            t1 = t.nv
            kt1 = t1.val
            t.nv = c
            fc = c.val
            c = t
            t = t1
            k = (c.val)
        zz = None
    l.head = t
    # while z is not None:
        # print(z.val)
        # z = z.nv
    # print("-"*10)
c=l.head
while c is not None:
    # print(c.val)
    c = c.nv

r(l,4)
c = l.head
while c is not None:
    print(c.val)
    c = c.nv












