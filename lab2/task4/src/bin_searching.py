import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', '..')
sys.path.insert(0, src_dir)

from utils import read_from_file, write_in_file, measuring

def bin_searching(mass, what_find):
    l = 0
    r = len(mass) - 1
    while l <= r:
        mid = (l + r) // 2
        if what_find == mass[mid]:
            return mid
        elif what_find < mass[mid]:
            r = mid - 1
        else:
            l = mid + 1
    return -1


def start_search(mass, mass_find):
    return [bin_searching(mass, mass_find[i]) for i in range(len(mass_find))]

if __name__ == '__main__':
    data = read_from_file('lab2/task4/txtf/input.txt')
    n = int(data[0]) 
    mass = data[1:n]
    k = int(data[n+1])
    mass_find = data[n+2: n+k+2]
    result = start_search(mass, mass_find)

    write_in_file('lab2/task4/txtf/output.txt', result)

    measuring(start_search, mass, mass_find)