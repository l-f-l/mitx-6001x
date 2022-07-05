def isIn(char, aStr):
    """

    :param char: a single character
    :param aStr: an alphabetized string
    :return: True is char is in aStr; False otherwise
    """
    if aStr == '':
        return False

    if len(aStr) == 1:
        return aStr == char

    midIndex = len(aStr) // 2
    midChar = aStr[midIndex]
    if char == midChar:
        return True

    elif char < midChar:
        return isIn(char, aStr[:midIndex])

    else:
        return isIn(char, aStr[midIndex + 1:])
