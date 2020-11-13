class Stack:
    def __init__(self, ma=10000):
        self.s = [None] * ma
        self.last = -1
        self.ma = ma

    def isEmpty(self):
        if self.last < 0:
            return True
        return False

    def isFull(self):
        if self.last + 1 == self.ma:
            return True
        return False

    def push(self, val):
        if self.isFull():
            raise Exception("Stack is full")
        else:
            self.last += 1
            self.s[self.last] = val

    def peek(self):
        if not self.isEmpty():
            return self.s[self.last]
        else:
            return

    def pop(self):
        if not self.isEmpty():
            self.last -= 1
            return self.s[self.last + 1]
        else:
            raise Exception("Stack is empty")

    def __str__(self):
        return "{} {}".format(self.last+1,self.s)