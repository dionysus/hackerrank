#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):

    arr_len = len(arr)
    i = 0
    swaps = 0
    ordered = False

    print("i: %d, swaps: %d" %(i, swaps))
    print(arr)
    print("---------")

    while not ordered and i < arr_len - 1:

        if arr[i] == i + 1:
            i += 1

        else:
            max_off = i
            inc_i = True
            ordered = True
            swap = False

            for j in range(i + 1, arr_len):

                # test for order
                if arr[j] < arr[j-1]:
                    ordered = False

                if arr[i] > arr[j]:
                    inc_i = False
                    swap = True
                    if arr[j] < arr[j-1]:
                        max_off = j

            if swap:
                arr[i], arr[max_off] = arr[max_off], arr[i]
                swaps += 1

            if inc_i:
                i += 1

        print ("i: %d, swaps: %d" %(i, swaps))
        print(arr)
        print("---------")

    return swaps


if __name__ == '__main__':

    # arr = [i for i in range(1, 11)]
    # random.seed(1)
    # random.shuffle(arr)
    # print(arr)

    # arr = [1, 3, 5, 2, 4, 6, 7]
    arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    res = minimumSwaps(arr)

    print(res)
