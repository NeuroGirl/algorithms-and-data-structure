import sys
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(CURRENT_DIR, '..', '..')
sys.path.insert(0, SRC_DIR)

from utils import read_from_file, write_in_file, measuring

def is_a_heap(arr: list) -> str:
    n = len(arr)
    for i in range(n):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[i] > arr[left]:
            return "NO"
        if right < n and arr[i] > arr[right]:
            return "NO"
    return "YES"

if __name__ == '__main__':
    data = read_from_file(0, 'lab5/task1/txtf/input.txt')
    versitiles = data[1:]
    result = is_a_heap(versitiles)
    write_in_file('lab5/task1/txtf/output.txt', result)

    measuring(1e2, is_a_heap, versitiles)