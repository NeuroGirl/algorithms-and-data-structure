import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', '..')
sys.path.insert(0, src_dir)

from utils import read_from_file, write_in_file, measuring
from task1.src.quick_sort import quick_sort


def hirsch_index(citations):
    n = len(citations)
    quick_sort(citations, 0, n-1)
    for h in range(n):
        if (n - h) <= int(citations[h]):
            return n - h
    return 0


if __name__ == '__main__':
    data = read_from_file('lab3/task5/txtf/input.txt')

    result = hirsch_index(data)

    write_in_file('lab3/task5/txtf/output.txt', [result])

    measuring(hirsch_index, data)