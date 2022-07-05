def gcdRecur(a, b):
    """

    :param a: a positive integer
    :param b: a positive integer
    :return: a positive integer, the greatest common divisor of a & b
    """
    if b == 0:
        return a

    return gcdRecur(b, a % b)
