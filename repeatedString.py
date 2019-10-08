def repeatedString(s, n):
    """
    :param s: a string to repeat
    :param n: the number of characters to consider
    :return: int

    >>> s = 'aba'
    >>> n = 10
    >>> repeatedString(s, n)
    7

    """

    return (n // len(s)) * s.count('a') + s[0: n % len(s)].count('a')
