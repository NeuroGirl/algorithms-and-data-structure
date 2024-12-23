import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', '..')
sys.path.insert(0, src_dir)

from utils import read_from_file, write_in_file, measuring

def majority_finder(a):
    dic = {}
    for i in a:
        dic[i] = dic.get(i, 0) + 1
    for k, v in dic.items():
        if v > len(a) // 2:
            return 1
    return 0

if __name__ == '__main__':
    data = read_from_file('lab2/task5/txtf/input.txt')
    n = data[0] 
    array = data[1:]
    result = majority_finder(array)

    write_in_file('lab2/task5/txtf/output.txt', str(result))

    measuring(majority_finder, array)
