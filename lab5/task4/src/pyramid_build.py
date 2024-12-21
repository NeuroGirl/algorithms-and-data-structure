import sys
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(CURRENT_DIR, '..', '..')
sys.path.insert(0, SRC_DIR)

from utils import read_from_file, write_in_file, measuring

def create_heap(n, A):

    swaps = []  # массив с перестановками

    def min_heap(i):
        min_index = i
        left = 2 * i + 1  # Левый ребенок
        right = 2 * i + 2  # Правый ребенок

        if left < n and A[left] < A[min_index]:
            min_index = left
        if right < n and A[right] < A[min_index]:
            min_index = right

        # Если ребенок меньше текущего узла, то меняем их местами
        if i != min_index:
            A[i], A[min_index] = A[min_index], A[i]
            swaps.append(f"{i} {min_index}\n")
            min_heap(min_index)

    for i in range(n // 2 - 1, -1, -1):
        min_heap(i)

    return swaps

if __name__ == '__main__':
    data = read_from_file(0, 'lab5/task4/txtf/input.txt')
    n = int(data[0])
    versitiles = [int(x) for x in data[1:]]
    result = create_heap(n, versitiles)
    result.insert(0, str(len(result))+'\n')
    write_in_file('lab5/task4/txtf/output.txt', result)

    measuring(1e2, create_heap, n, versitiles)