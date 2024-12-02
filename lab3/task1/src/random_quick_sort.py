import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', '..')
sys.path.insert(0, src_dir)

import random
from utils import read_from_file, write_in_file, measuring


def partition(A, l, r):
    x = A[l]
    j = l
    for i in range(l+1, r+1):
        if A[i] < x:
            j += 1
            A[j], A[i] = A[i], A[j]
    A[l], A[j] = A[j], A[l]
    return j


def randomized_quick_sort(A, l, r):
    if l < r:
        k = random.randint(l, r)
        A[l], A[k] = A[k], A[l]
        m = partition(A, l, r)
        randomized_quick_sort(A, l, m-1)
        randomized_quick_sort(A, m+1, r)
    return A


if __name__ == '__main__':
    data = read_from_file('lab3/task1/txtf/input.txt')

    n, array = data[0], data[1:]
    result = randomized_quick_sort(array, 0, len(array) - 1)

    write_in_file('lab3/task1/txtf/output.txt', result)

    measuring(randomized_quick_sort, array, 0, len(array) - 1)