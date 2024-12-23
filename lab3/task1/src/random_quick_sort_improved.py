import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', '..')
sys.path.insert(0, src_dir)

import random
from utils import read_from_file, write_in_file, measuring


def partition3(arr, l, r):
    x = arr[l]
    m1 = l
    m2 = r
    i = l
    while i <= m2:
        if arr[i] < x:
            arr[m1], arr[i] = arr[i], arr[m1]
            m1 += 1
            i += 1
        elif arr[i] > x:
            arr[i], arr[m2] = arr[m2], arr[i]
            m2 -= 1
        else:
            i += 1
    return m1, m2


def randomized_quick_sort_p3(arr, l, r):
    if l < r:
        k = random.randint(l, r)
        arr[l], arr[k] = arr[k], arr[l]
        m1, m2 = partition3(arr, l, r)
        randomized_quick_sort_p3(arr, l, m1-1)
        randomized_quick_sort_p3(arr, m2+1, r)
    return arr


if __name__ == '__main__':
    data = read_from_file('lab3/task1/txtf/input.txt')

    n, array = data[0], data[1:]
    result = randomized_quick_sort_p3(array, 0, len(array) - 1)

    write_in_file('lab3/task1/txtf/output.txt', result)

    measuring(randomized_quick_sort_p3, array, 0, len(array) - 1)