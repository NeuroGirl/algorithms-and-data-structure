import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', '..')
print(src_dir)
sys.path.insert(0, src_dir)

from utils import open_close, write

def majority_finder(a):
    dic = {}
    for i in a:
        dic[i] = dic.get(i, 0) + 1
    for k, v in dic.items():
        if v > len(a) // 2:
            return 1
    return 0


nums = open_close(5, 1)
list_input = nums[1]
write(5, str(majority_finder(list(map(int, list(list_input.split(' ')))))))