import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', '..')
sys.path.insert(0, src_dir)

from utils import *

def sort_merge(nums):
    if len(nums) > 1:
        middle = len(nums) // 2
        left = nums[:middle]
        right = nums[middle:]
        sort_merge(left)
        sort_merge(right)

        p = r = q = 0
        while (p < len(left)) and (r < len(right)):
            if left[p] < right[r]:
                nums[q] = left[p]
                p += 1
            else:
                nums[q] = right[r]
                r += 1
            q += 1

        while p < len(left):
            nums[q] = left[p]
            p += 1
            q += 1
        while r < len(right):
            nums[q] = right[r]
            r += 1
            q += 1
    return nums

if __name__ == '__main__':
    data = read_from_file('lab2/task1/txtf/input.txt')

    n, array = data[0], data[1:]
    result = sort_merge(array)

    write_in_file('lab2/task1/txtf/output.txt', result)

    measuring(sort_merge, array)