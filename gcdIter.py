def gcdIter(a, b):
    """

    :param a: a positive integer
    :param b: a positive integer
    :return: a positive integer, the greatest common divisor of a & b.
    """
    testValue = min(a, b)

    while a % testValue != 0 or b % testValue != 0:
        testValue -= 1

    return testValue
