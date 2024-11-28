import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', '..')
sys.path.insert(0, src_dir)

import random
from utils import read_from_file, write_in_file, measuring


def partition3(A, l, r):
    x = A[l]
    m1 = l
    m2 = r
    i = l
    while i <= m2:
        if A[i] < x:
            A[m1], A[i] = A[i], A[m1]
            m1 += 1
            i += 1
        elif A[i] > x:
            A[i], A[m2] = A[m2], A[i]
            m2 -= 1
        else:
            i += 1
    return m1, m2


def randomized_quick_sort_p3(A, l, r):
    if l < r:
        k = random.randint(l, r)
        A[l], A[k] = A[k], A[l]
        m1, m2 = partition3(A, l, r)
        randomized_quick_sort_p3(A, l, m1-1)
        randomized_quick_sort_p3(A, m2+1, r)
    return A


if __name__ == '__main__':
    data = read_from_file('algorithms-and-data-structures/lab3/task1/txtf/input.txt')

    n, array = data[0], data[1:]
    result = randomized_quick_sort_p3(array, 0, len(array) - 1)

    write_in_file('algorithms-and-data-structures/lab3/task1/txtf/output.txt', result)

    measuring(randomized_quick_sort_p3, array, 0, len(array) - 1)