#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    arr_len = len(arr)

    if arr_len == 1:
        return 0

    swap_i = 0
    min_num = arr[0]
    swap = False

    for i in range(1, arr_len):

        if arr[0] > arr[i]:
            swap = True
            if arr[i] < arr[i - 1]:
                swap_i = i
        if arr[i] < min_num:
            min_num = arr[i]

    add = 0

    if swap:
        arr[0], arr[swap_i] = arr[swap_i], arr[0]
        add = 1

    # print(arr)

    if arr[0] > min_num:
        return minimumSwaps(arr) + add
    else:
        return minimumSwaps(arr[1:]) + add


if __name__ == '__main__':

    # arr = [i for i in range(1, 11)]
    # random.seed(1)
    # random.shuffle(arr)
    # print(arr)
    # arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    arr = [7, 1, 3, 2, 4, 5, 6]
    res = minimumSwaps(arr)
    print(res)
    print("---------------")

    arr = [4, 3, 1, 2]
    res = minimumSwaps(arr)
    print(res)
    print("---------------")

    arr = [2, 3, 4, 1, 5]
    res = minimumSwaps(arr)
    print(res)
    print("---------------")

    arr = [1, 3, 5, 2, 4, 6, 7]
    res = minimumSwaps(arr)
    print(res)

