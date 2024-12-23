import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', '..')
sys.path.insert(0, src_dir)

from utils import read_from_file, write_in_file, measuring


def partition(a, l, r):
    x = a[l]
    j = l
    for i in range(l+1, r+1):
        if a[i] < x:
            j += 1
            a[j], a[i] = a[i], a[j]
    a[l], a[j] = a[j], a[l]
    return j


def quick_sort(a, l, r):
    if l < r:
        j = partition(a, l, r)
        quick_sort(a, l, j-1)
        quick_sort(a, j+1, r)
    return a


if __name__ == '__main__':
    data = read_from_file('lab3/task1/txtf/input.txt')

    n, array = data[0], data[1:]
    result = quick_sort(array, 0, len(array) - 1)

    write_in_file('lab3/task1/txtf/output.txt', result)

    measuring(quick_sort, array, 0, len(array) - 1)