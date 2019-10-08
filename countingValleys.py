def countingValleys(n, s):
    """
    >>> n = 8
    >>> s = 'UDDDUDUU'
    >>> countingValleys(n, s)
    1
    """

    d = {'U': 1, 'D': -1}

    point = 0
    valleys = 0

    for c in s:
        if point == -1 and c == 'U':
            valleys += 1
        point += d[c]

    return valleys
