import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', '..')
sys.path.insert(0, src_dir)

from utils import read_from_file, write_in_file, measuring


def qsort(a, left, right):
    key = a[(left+right)//2]
    i = left
    j = right
    while i <= j:
        while a[i] < key:
            i += 1
        while a[j] > key:
            j -= 1
        if i <= j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
    if left < j:
        qsort(a, left, j)
    if i < right:
        qsort(a, i, right)
    return a


def anti_quick_sort(n):
    a = [i+1 for i in range(n)]
    for i in range(2, len(a)):
        a[i], a[i//2] = a[i//2], a[i]
    return a


if __name__ == '__main__':
    data = read_from_file('lab3/task2/txtf/input.txt')

    n = data[0]
    result = anti_quick_sort(int(n))

    write_in_file('lab3/task2/txtf/output.txt', result)

    measuring(anti_quick_sort, int(n))