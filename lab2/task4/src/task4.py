import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', '..')
print(src_dir)
sys.path.insert(0, src_dir)

from utils import open_close, write

file = open_close(4, 2)
mass, mass_find = file[1], file[3]
n, mass = file[0], list(map(int, list(mass.split(' '))))
k, mass_find = file[2], list(map(int, list(mass_find.split(' '))))

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

write(4, ' '.join(map(str, start_search(mass, mass_find))))