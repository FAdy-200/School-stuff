# CSE314- Assignment 1
#
# Topic: Review of Python Basics
# Author : FirstName LastName
# Date : 02/ 11/ 2020
# Exercise 1: calculate average
def listAvg(li):
    """
    This function takes a list li and returns it is average.
    if the users inputs is invalid the function returns The input is invalid
    :param li: list
    :return: average of a list
    """
    try:
        return sum(li) / len(li)
    except:
        return "The input is invalid"


# Exercise 2: calculate average
def vowelsCounter(s):
    """
    this function takes a string s and returns the number of vowels in it in two ways one is by using Regex and one is
    hard coded.
    it also checks for invalid input and prints out The input is invalid
    :param s: str
    :return: int
    """
    try:  # trying to usse Regex if available
        vowels = r"[aeiouyAEIOUY]"  # English Vowels
        import re  # importing the Regex library
        if type(s) == str:  # checking if the inputs type is string
            x = re.findall(vowels, s)  # using Regex to find all matches of vowels, it returns a list with all matches
            return len(x)  # returning the length of x
        else:
            return "The input is invalid"
    except:
        vowels = "aeiouyAEIOUY"
        z = 0  # number of vowels in the start
        if type(s) == str:  # checking if the inputs type is string
            for i in s:  # iterating through the string
                if i in vowels:  # checking if the character i is in vowels
                    z += 1  # incrementing the number of vowels
            return z  # returns the number of vowels
        else:
            return "The input is invalid"


# Exercise 3: Variable swapping
def swap(x, y):
    """
    This function takes two variables and swaps their places
    :param x: int or float
    :param y: int or float
    :return: tuple
    """
    aceptedInputs = [int, float]
    if type(x) == type(y) in aceptedInputs:
        y, x = x, y
        return x, y
    else:
        return "The input is invalid"


def odd(n):
    for i in range(1, n + 1, 2):
        print(i, end=" ")
