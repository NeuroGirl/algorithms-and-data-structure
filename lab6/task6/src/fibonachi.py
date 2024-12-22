import sys
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(CURRENT_DIR, '..', '..')
sys.path.insert(0, SRC_DIR)

from utils import read_from_file, write_in_file, measuring

def is_perfect_square(n):
    root = int(n ** 0.5)
    return root * root == n


def fibonachi(array):
    results = []
    for n in array:
        n = int(n)
        if is_perfect_square(5 * n**2 + 4) or is_perfect_square(5 * n**2 - 4):
            results.append('Yes\n')
        else:
            results.append('No\n')
    return results


if __name__ == '__main__':
    data = read_from_file(0, 'lab6/task6/txtf/input.txt')
    result = fibonachi(data[1:])
    write_in_file('lab6/task6/txtf/output.txt', result)

    measuring(1e2, fibonachi, data)