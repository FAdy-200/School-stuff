import math


def polygon_perimeter(n_sides: int, side_len: int) -> int:
    """
    calculates the perimeter of the shape
    :param n_sides: number of sides
    :param side_len: length of polygon sides
    :return: perimeter of the shape
    >>> polygon_perimeter(4,5)
    20
    """
    perimeter = n_sides * side_len
    return perimeter


def polygon_apothem(n_sides: int, side_len: int) -> float:
    """
    calculates the apothem of the shape
    :param n_sides: number of sides
    :param side_len: length of polygon sides
    :return: apothem of the shape
    >>> polygon_apothem(4,5)
    2.5000000000000004
    """
    denominator = 2 * math.tan(math.pi / n_sides)
    apothem = side_len / denominator
    return apothem


def polygon_area(n_sides: int, side_len: int) -> float:
    """
    Find the area of a regular polygon
    :param n_sides: number of sides
    :param side_len: length of polygon sides
    :return: area of polygon
    >>> round(polygon_area(4, 5))
    25
    """
    perimeter = polygon_perimeter(n_sides, side_len)
    apothem = polygon_apothem(n_sides, side_len)
    area = perimeter * apothem / 2
    return area


# polygon_area(4, 5)
