class Mother():

    def pr(self):
        print("Mother")

    def prm(self):
        print("Mother")


class Father():

    def pr(self):
        print("Father")


class Child(Father, Mother):
    pass


a = Child()
a.pr()
a.prm()




class one():
    def fun1(self):
        print("one")
class two():
    def fun1(self):
        print("two")
    def fun2(self):
        print("two")
class tez(one,two):
    pass

nawwar = tez()
nawwar.fun1()
nawwar.fun2()
"""
in multiple inheritance the child class takes two other classes as parent classes and inherits both of their functions 
but if a function exist in both classes it takes the function from the first class in the parenthesis    
"""