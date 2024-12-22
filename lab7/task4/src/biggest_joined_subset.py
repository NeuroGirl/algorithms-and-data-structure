import sys
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(CURRENT_DIR, '..', '..')
sys.path.insert(0, SRC_DIR)

from utils import read_from_file, write_in_file, measuring

def biggest_joined_subset(number1: list[int], number2: list[int]) -> int:
    counts = [[0] * (len(number2) + 1) for _ in range(len(number1) + 1)]

    for i in range(1, len(number1) + 1):
        for j in range(1, len(number2) + 1):
            if number1[i - 1] == number2[j - 1]:
                counts[i][j] = counts[i - 1][j - 1] + 1
            else:
                counts[i][j] = max(counts[i][j - 1], counts[i - 1][j])
    return counts[len(number1)][len(number2)]

if __name__ == '__main__':
    data = read_from_file(0, 'lab7/task4/txtf/input.txt')
    n = int(data[0])
    array_1 = data[1:n+1]
    m = int(data[n+1])
    array_2 = data[n+2:n+m+2]
    result = str(biggest_joined_subset(array_1, array_2))
    write_in_file('lab7/task4/txtf/output.txt', result)

    measuring(1e2, biggest_joined_subset, array_1, array_2)