def hourglassSum(arr):
    """
    >>> arr = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    >>> hourglassSum(arr)
    7
    >>> arr = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]
    >>> hourglassSum(arr)
    19
    """

    max_sum = None

    for a in range(0, 4):
        for b in range(0, 4):
            curr = helper(a, b, arr)
            if max_sum is None:
                max_sum = curr
            else:
                max_sum = max(max_sum, curr)

    return max_sum


def helper(a, b, arr):

    sum = 0

    for i in range(0, 3):
        for j in range(0, 3):
            if not(i == 1 and (j == 0 or j == 2)):
                sum += arr[i + a][j + b]
    return sum
