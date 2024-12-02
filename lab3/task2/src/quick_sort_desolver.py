import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', '..')
sys.path.insert(0, src_dir)

from utils import read_from_file, write_in_file, measuring

def quick_sort_desolver(n):
    a = [i for i in range(1, n+1)]
    for i in range(2, len(a)):
        a[i], a[i//2] = a[i//2], a[i]
    return a


if __name__ == '__main__':
    data = read_from_file('lab3/task2/txtf/input.txt')

    n = data[0]
    result = quick_sort_desolver(int(n))

    write_in_file('lab3/task2/txtf/output.txt', result)

    measuring(quick_sort_desolver, int(n))