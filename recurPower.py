def recurPower(base, exp):
    """

    param base: int or float.
    param exp: int >= 0
    return: int or float, base^exp
    """
    if exp <= 0:
        return 1
    return base * recurPower(base, exp - 1)
