# CSE314- Assignment 1
#
# Topic: Review of Python Basics
# Author : Fadi Alahmad
# Date : 02/ 11/ 2020
# Exercise 1: calculate average
def listAvg(li):
    """
    This function takes a list li and returns it is average.
    if the users inputs is invalid the function returns The input is invalid
    :param li: list
    :return: float
    """
    try:
        return sum(li) / len(li)
    except:
        return "The input is invalid"


# Exercise 2: Vowel counter
def vowelsCounter(s):
    """
    this function takes a string s and returns the number of vowels in it in two ways one is by using Regex and one is
    hard coded.
    it also checks for invalid input and prints out The input is invalid
    :param s: str
    :return: int
    """
    try:  # trying to use Regex if available
        vowels = r"[aeiouyAEIOUY]"  # English Vowels as a Regex pattern
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
    :param x:
    :param y:
    :return: tuple
    """
    y, x = x, y
    return x, y


# Exercise 4: printing the odd numbers upto N
def odd(n):
    """
    this function takes an integer n and prints the odd numbers upto n by generating an integer that starts from1
    to n+1 with a step of 2
    :param n: int
    :return: None
    """
    try:
        for i in range(1, n + 1, 2):
            print(i, end=" ")
    except:
        print("Input is invalid")


# Exercise 5: calculating the volume of a sphere
def vol(r):
    """
    this function takes the radius of a sphere as an input and calculates its volume
    :param r: int or float
    :return: float
    """
    aceptedInputs = [int, float]  # list of accepted input types
    if type(r) in aceptedInputs:  # checking if the inputs type is in the list
        return (4 / 3) * 3.14 * r ** 3  # performing the calculations
    else:
        return "input is invalid"


# Exercise 6: GCD
def gcd(a, b):
    """
    this function takes two inputs and uses Euclidean algorithm to do so
    :param a: int
    :param b: int
    :return: int
    """
    if b == 0:  # checking if the reminder is equal to zero
        return a
    else:
        return gcd(b, b % a)  # calling the same function but with swapping and applying the modulus operator
