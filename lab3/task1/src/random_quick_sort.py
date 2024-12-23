import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', '..')
sys.path.insert(0, src_dir)

import random
from utils import read_from_file, write_in_file, measuring


def partition(arr, l, r):
    x = arr[l]
    j = l
    for i in range(l+1, r+1):
        if arr[i] < x:
            j += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[l], arr[j] = arr[j], arr[l]
    return j


def randomized_quick_sort(arr, l, r):
    if l < r:
        k = random.randint(l, r)
        arr[l], arr[k] = arr[k], arr[l]
        m = partition(arr, l, r)
        randomized_quick_sort(arr, l, m-1)
        randomized_quick_sort(arr, m+1, r)
    return arr


if __name__ == '__main__':
    data = read_from_file('lab3/task1/txtf/input.txt')

    n, array = data[0], data[1:]
    result = randomized_quick_sort(array, 0, len(array) - 1)

    write_in_file('lab3/task1/txtf/output.txt', result)

    measuring(randomized_quick_sort, array, 0, len(array) - 1)