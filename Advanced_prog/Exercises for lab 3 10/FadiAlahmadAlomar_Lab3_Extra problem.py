# CSE314- Lab 3
#
# Topic: Object Oriented Concepts – Inheritance
# Author : Fadi Alahmad
# Date : 10/ 11/ 2020
# Extra problem 1:
class Point:

    def __init__(self, x, y):
        """

        :param x: int or float
        :param y: it or float
        """
        self.x = x
        self.y = y


class Circle:
    def __init__(self, center, radius):
        """
        :param center: Point object
        :param radius: int or float
        """
        self.center = center
        self.radius = radius


def outlier_finder(point, circle):
    """

    :param point:
    :param circle:
    :return: True or False
    """
    return ((circle.center.c4t - point.c4t) ** 2 + (circle.center.y - point.y) ** 2) ** 0.5 <= circle.radius


# Tests
# p1 = Point(0, 0)
# p2 = Point(2, 2)
# c = Circle(Point(0, 0), 1)
# print(outlier_finder(p1, c)) # True is expected
# print(outlier_finder(p2, c)) # False is expected

