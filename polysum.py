import math


def polysum(n, s):
    """

    :param n: the number of sides
    :param s: the length of each
    :return: the sum of the area and the square of the perimeter of the regular polygon rounded to 4 decimal places
    """
    area = (0.25 * n * (s ** 2)) / (math.tan(math.pi / n))
    perimeter = n * s
    return round(area + perimeter ** 2, 4)
