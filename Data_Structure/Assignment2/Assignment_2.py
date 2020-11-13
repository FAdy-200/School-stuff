import Data_Structure.Assignment2.Stack as Stack

# Question 2
s1 = "[()]{}{[()()]()}"
s2 = "[(])"


def expressionChecker(s):
    myStack = Stack.Stack()
    op = ["{", "[", "("]
    cl = ["{}", "[]", "()"]
    for i in s:
        if i in op:
            myStack.push(i)
        else:
            if myStack.peek() is not None:
                if myStack.peek() + i in cl:
                    myStack.pop()
                else:
                    return "input is invalid"
            else:
                return "input is invalid"
    return "input is valid"


print(expressionChecker(s1))
print(expressionChecker(s2))


# Question 6:

def Sum(stack):
    auxStack = Stack.Stack()
    s = 0
    while stack.last >= 0:
        p = stack.pop()
        s += p
        auxStack.push(p)
    while auxStack.last >= 0:
        stack.push(auxStack.pop())
    return s


myStack = Stack.Stack()
for i in range(1, 101):
    myStack.push(i)
print(Sum(myStack))
print(myStack)
# Question 7

s71 = "abcddcba"
s72 = "Fady"
s73 = "abcddcbaa"


def palindromeCheck(s):
    myStack = Stack.Stack()
    for i in s:
        myStack.push(i)
    for i in s:
        if i != myStack.pop():
            return False
    return True



print(palindromeCheck(s71))
print(palindromeCheck(s72))
print(palindromeCheck(s73))


# Question 8


def insert_sorted(stack, val):
    auxStack = Stack.Stack(5)
    while stack.last >= 0 and val > stack.peek():
        auxStack.push(stack.pop())
    stack.push(val)
    while auxStack.last >= 0:
        stack.push(auxStack.pop())
    return stack

st = Stack.Stack(5)
print(insert_sorted(st, 12))
print(insert_sorted(st, 10))
print(insert_sorted(st, 1000))
print(insert_sorted(st, 1))
