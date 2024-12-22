import sys
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(CURRENT_DIR, '..', '..')
sys.path.insert(0, SRC_DIR)

from utils import read_from_file, write_in_file, measuring

def variety(data):
    result = []
    current_set = set()
    for x in range(0, len(data),2):
        operation, n = data[x], data[x+1]
        if operation == 'A':
            current_set.add(n)
        elif operation == 'D':
            current_set.discard(n)
        elif operation == '?':
            if n in current_set:
                result.append('Y\n')
            else:
                result.append('N\n')
    return result


if __name__ == '__main__':
    data = read_from_file(0, 'lab6/task1/txtf/input.txt')
    versitiles = data[1:]
    result = variety(versitiles)
    write_in_file('lab6/task1/txtf/output.txt', result)

    measuring(1e2, variety, versitiles)