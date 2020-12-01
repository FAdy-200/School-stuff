# CSE314- Lab 5
#
# Topic: Design patterns II
# Author : Fadi Alahmad
# Date : 01/ 12/ 2020
# Problem 1:
class Duck:
    def quack(self):
        print("Quack")

    def fly(self):
        print("I'm flying")


class Turkey:
    def gobble(self):
        print("Gobble Gobble")

    def fly(self):
        print("I'm flying a short distance")


class TurkeyAdapter(Turkey):
    """
    this class takes the turkey class and adapts it to the duck calss
    """

    def __init__(self, adaptee):
        """
        :param adaptee: Turkey instance
        """
        self.adaptee = adaptee

    def quack(self):
        """
        :calls: gobble function of the adaptee which is a Turkey instance
        """
        self.adaptee.gobble()

    def fly(self):
        """
        :calls: 5 times the fly function of the adaptee which is a Turkey instance
        """
        for _ in range(5):
            self.adaptee.fly()


def duck_interaction(duck):
    duck.quack()
    duck.fly()


duck = Duck()
turkey = Turkey()
turkey_adapter = TurkeyAdapter(turkey)

print("The Turkey says")
turkey.gobble()
turkey.fly()

print("\nThe Duck says")
duck.quack()
duck.fly()

print("\nthe Turkey_Adapter says")
duck_interaction(turkey_adapter)
"""
Expected output:
The Turkey says
Gobble Gobble
I'm flying a short distance

The Duck says
Quack
I'm flying

the Turkey_Adapter says
Gobble Gobble
I'm flying a short distance
I'm flying a short distance
I'm flying a short distance
I'm flying a short distance
I'm flying a short distance
"""
