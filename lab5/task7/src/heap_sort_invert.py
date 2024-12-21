import sys
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(CURRENT_DIR, '..', '..')
sys.path.insert(0, SRC_DIR)

from utils import read_from_file, write_in_file, measuring

def heapify(arr: list, n: int, i: int) -> None:
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] < arr[largest]:
        largest = left
    if right < n and arr[right] < arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr: list) -> list:
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

if __name__ == '__main__':
    data = read_from_file(0, 'lab5/task7/txtf/input.txt')
    result = heap_sort(data)
    new_result = [result[0]]
    for elem in result[1:]:
        new_result.append(f' {elem}')
    write_in_file('lab5/task7/txtf/output.txt', new_result)

    measuring(1e2, heap_sort, data)