# CSE314- Lab 4 Extra
#
# Topic: Object Oriented Concepts
# Author : Fadi Alahmad
# Date : 17/ 11/ 2020
# Exercise 0:
"""
ERROR Account has no attribute account_holder
Billy
Yes!
Yes!
Have a nice day!
"""


# Exercise 1:
class Person:
    def __init__(self, name):
        self.name = name
        self.last_said = "Why are we here?"

    def say(self, stuff):
        self.last_said = stuff
        return stuff

    def ask(self, stuff):
        return self.say("Would you please " + stuff)

    def greet(self):
        return self.say("Hello, my name is " + self.name)

    def repeat(self):
        return self.last_said


john = Person("John")
print(
    john.repeat() + "\n" +
    john.say("Hello") + "\n" +
    john.repeat() + "\n" +
    john.greet() + "\n" +
    john.repeat() + "\n" +
    john.ask("preserve abstraction barriers") + "\n" +
    john.repeat())


# Exercise 2:
# the following implementation will work as intended
class DoubleTalker(Person):
    def __init__(self, name):
        Person.__init__(self, name)

    def say(self, stuff):
        return Person.say(self, stuff) + " " + self.repeat()


# steven = DoubleTalker("Steven")
# print(steven.say("hello"))
# print(steven.repeat())
"""
# the following implementation will return a different result
# as if we call the repeat function it will not repeat it will print the initializer for the repeat

"""


class DoubleTalker(Person):
    def __init__(self, name):
        Person.__init__(self, name)

    def say(self, stuff):
        return stuff + " " + stuff


# steven = DoubleTalker("Steven")
# print(steven.say("hello"))
# print(steven.say("hello"))
# print(steven.repeat())

# Exercise 4:

class Account(object):
    """A bank account that allows deposits and withdrawals."""
    interest = 0.02

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder

    def deposit(self, amount):
        """Increase the account balance by amount and return the new
        balance."""
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        """Decrease the account balance by amount and return the new
        balance."""
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance


class CheckingAccount(Account):
    """A bank account that charges for withdrawals."""
    withdraw_fee = 1
    interest = 0.01

    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_fee)
