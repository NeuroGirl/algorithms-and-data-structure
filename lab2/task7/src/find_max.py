import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', '..')
sys.path.insert(0, src_dir)

from utils import read_from_file, write_in_file, measuring

def find_max(a):
    max_sum, summ = 0, 0
    for i in range(len(a)):
        if summ == 0:
            start_indx = i
        summ += int(a[i])
        if max_sum < summ:
            max_sum = summ
            end_indx = i
        if summ < 0:
            summ = 0
    return a[start_indx:end_indx + 1]

if __name__ == '__main__':
    data = read_from_file('lab2/task7/txtf/input.txt')
    array = data[0:]
    result = find_max(array)

    write_in_file('lab2/task7/txtf/output.txt', result)

    measuring(find_max, array)
