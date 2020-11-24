# CSE314- Lab 3
#
# Topic: Object Oriented Concepts – Inheritance
# Author : Fadi Alahmad
# Date : 10/ 11/ 2020
# Problem 1:
class Spell:
    def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation

    def __str__(self):
        return self.name + '' + self.incantation + ' \n ' + self.get_description()

    def get_description(self):
        return 'No description'

    def execute(self):
        print(self.incantation)


class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'SummoningCharm')

    def get_description(self):
        return 'This charm summons an object to the caster, potentially over a significant distance?.'


class Confundo(Spell):
    def __init__(self):
        Spell.__init__(self, 'Confundo', 'ConfundusCharm')

    def get_description(self):
        return 'Cause the victim to become confused and befuddled.'


def study_spell(spell):
    print(spell)


"""
1. parent class is Spell, child classes are Accio Confundo
2. 
    Accio
    SummoningCharm Accio
    'No description'
    ConfundusCharm Confundo
    Cause the victim to become confused and befuddled.
3. the one within the class Confundo as it stands higer in the hierarchy of functions  
4. we need to add the following function to the class Accio
    def get_description(self):
        return 'This charm summons an object to the caster, potentially over a significant distance?.'
"""


# Problem 2
class Shape:
    def get_area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def get_area(self):
        return (self.length ** 2)


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.width * self.length


# Problem 3
class Address:
    def __init__(self, street, city):
        self.street = str(street)
        self.city = str(city)

    def show(self):
        print(self.street)
        print(self.city)


class Person:
    def __init__(self, name, email):
        self.name = str(name)
        self.email = str(email)

    def show(self):
        print(self.name + ' ' + self.email)


class Contact(Person, Address):
    def __init__(self, name, email, street, address):
        """
        this function doesnt use the super() function as the super will only point to tge Person class thus we need
        to specify which class takes what parameters as initializers
        :param name: str
        :param email: str
        :param street: str
        :param address: str
        """
        Person.__init__(self, name, email)
        Address.__init__(self, street, address)

    def show(self):
        Person.show(self)
        Address.show(self)


# Tests
# Exercise 1
# spell = Accio()
# spell.execute()  # will print Accio
# study_spell(spell)  # will print SummoningCharmAccio \n This charm summons an object to the caster, potentially over a significant distance?.
# study_spell(Confundo()) # will print ConfundusCharmConfundo \n Cause the victim to become confused and befuddled.
# Exercise 2
# s = Square(2)
# s.get_area() # 4 is expected as an output
# r = Rectangle(2,4)
# r.get_area() # 8 is expected as an output
# Exercise 3
# s = Contact("fadi", "fadi.alahmad@ejust.edu.eg", "sinosi street", "alex")
# s.show() # will print fadi fadi.alahmad@ejust.edu.eg \n sinosi street \n alex
