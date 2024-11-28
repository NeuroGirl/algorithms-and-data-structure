import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', '..')
sys.path.insert(0, src_dir)

from utils import read_from_file, write_in_file, measuring


def scarecrow_sort(n, k, array):
    n, k = int(n), int(k)
    for i in range(0, n-k):
        if array[i] > array[i+k]:
            array[i], array[i+k] = array[i+k], array[i]
    return "YES" if array == sorted(array) else "NO"


if __name__ == '__main__':
    data = read_from_file('algorithms-and-data-structures/lab3/task3/txtf/input.txt')

    n, k = data[:2]
    array = data[2:]
    result = scarecrow_sort(n, k, array)

    write_in_file('algorithms-and-data-structures/lab3/task3/txtf/output.txt', [result])

    measuring(scarecrow_sort, n, k, array)