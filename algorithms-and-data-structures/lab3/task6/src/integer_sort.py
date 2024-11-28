import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', '..')
print(src_dir)
sys.path.insert(0, src_dir)

from utils import read_from_file, write_in_file, measuring


def quick_sort(A, l, r):
    if l < r:
        m = partition(A, l, r)
        quick_sort(A, l, m-1)
        quick_sort(A, m+1, r)


def partition(A, l, r):
    x = A[l]
    j = l
    for i in range(l+1, r+1):
        if A[i] <= x:
            j += 1
            A[j], A[i] = A[i], A[j]
    A[l], A[j] = A[j], A[l]
    return j


def sum_of_tenths(A, B):
    C = []
    for b in B:
        for a in A:
            C.append(int(a) * int(b))
    quick_sort(C, 0, len(C)-1)
    sum_of_tenths = sum(C[i] for i in range(0, len(C), 10))
    return sum_of_tenths


if __name__ == '__main__':
    data = read_from_file('algorithms-and-data-structures/lab3/task6/txtf/input.txt')

    n, m = data[:2]
    A = data[2:int(n) + 2]
    B = data[int(n) + 2:]
    result = sum_of_tenths(A, B)

    write_in_file('algorithms-and-data-structures/lab3/task6/txtf/output.txt', [result])

    measuring(sum_of_tenths, A, B)