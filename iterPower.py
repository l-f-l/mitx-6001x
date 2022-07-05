def iterPower(base, exp):
    """

    :param base: int or float.
    :param exp: int >= 0
    return: int or float, base^exp
    """
    result = 1
    while exp > 0:
        result *= base
        exp -= 1
    return result
