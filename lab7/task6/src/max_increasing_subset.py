import sys
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(CURRENT_DIR, '..', '..')
sys.path.insert(0, SRC_DIR)

from utils import read_from_file, write_in_file, measuring

def max_increasing_subsequence(numbers: list[str]) -> list[str]:
    n = len(numbers)
    if n == 0:
        return ["0\n"]

    counts = [1] * n
    pred = [-1] * n
    for i in range(1, n):
        for j in range(i):
            if int(numbers[j]) < int(numbers[i]):
                if counts[j] + 1 > counts[i]:
                    counts[i] = counts[j] + 1
                    pred[i] = j

    max_len = 0
    index = -1
    for i in range(n):
        if counts[i] > max_len:
            max_len = counts[i]
            index = i

    lis = []
    while index != -1:
        lis.append(numbers[index] + ' ')
        index = pred[index]
    lis.reverse()

    return [str(max_len) + '\n', *lis]

if __name__ == '__main__':
    data = read_from_file(0, 'lab7/task6/txtf/input.txt')
    result = max_increasing_subsequence(data[1:])
    write_in_file('lab7/task6/txtf/output.txt', result)

    measuring(1e2, max_increasing_subsequence, data)