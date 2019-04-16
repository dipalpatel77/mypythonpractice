def pos_neg(a, b, negative):
    """

    :rtype : object
    """
    if negative:
        return 1
        print('true', (a < 0 and b < 0))
    else:
        return 1
        print('false', ((a < 0 and b > 0) or (a > 0 and b < 0)))


pos_neg(-21, -2, negative=-5)