def jumpingOnClouds(c):
    """
    Return the minimum path to the end index.
    Each step can jump 1 or 2 indices, but can only land on a 0.

    >>> c = [0, 0, 1, 0, 0, 1, 0]
    >>> jumpingOnClouds(c)
    4
    >>> c = [0, 0]
    >>> jumpingOnClouds(c)
    1
    """

    if len(c) == 0:
        return 0

    if c[0] == 1:
        return -1

    if c[0] == 0:

        if len(c) == 1:
            return 0

        if len(c) > 2:
            more_jumps = jumpingOnClouds(c[2:])  # skip 2
        else:
            more_jumps = -1

        jumps = jumpingOnClouds(c[1:])  # skip 1

        if more_jumps == -1 and jumps == -1:
            return -1
        elif more_jumps == -1:
            return 1 + jumps
        elif jumps == -1:
            return 1 + more_jumps
        else:
            return 1 + min(jumps, more_jumps)
