import sys
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(CURRENT_DIR, '..', '..')
sys.path.insert(0, SRC_DIR)

from utils import read_from_file, write_in_file, measuring

def tree_height(n, parents):
    children = [[] for _ in range(n)]
    root = -1
    for child, parent in enumerate(parents):
        if parent != -1:
            children[parent].append(child)
        else:
            root = child

    def calc_height(node):
        if not children[node]:
            return 1
        max_height = 0
        for child in children[node]:
            max_height = max(max_height, calc_height(child))
        return max_height + 1

    return calc_height(root)

if __name__ == '__main__':
    data = read_from_file(0, 'lab5/task2/txtf/input.txt')
    n = int(data[0])
    versitiles = [int(x) for x in data[1:]]
    result = str(tree_height(n, versitiles))
    write_in_file('lab5/task2/txtf/output.txt', result)

    measuring(1e2, tree_height, n, versitiles)