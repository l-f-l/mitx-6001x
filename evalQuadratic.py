def evalQuadratic(a, b, c, x):
    """

    :param a, b, c: numerical values for the coefficients of a quadratic equation
    :param x: numerical value at which to evaluate the quadratic.
    :return: numerical value of the quadratic ax^2 + bx + c
    """
    return a * (x ** 2) + b * x + c
