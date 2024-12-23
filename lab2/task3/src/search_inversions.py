import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', '..')
sys.path.insert(0, src_dir)

from utils import read_from_file, write_in_file, measuring

def search(nums, nums_copy, l, mid, r):
    i = k = l
    j = mid + 1
    count_inf = 0

    while i <= mid and j <= r:
        if nums[i] <= nums[j]:
            nums_copy[k] = nums[i]
            i += 1
        else:
            nums_copy[k] = nums[j]
            j += 1
            count_inf += (mid - i + 1)
        k += 1

    while i <= mid:
        nums_copy[k] = nums[i]
        k += 1
        i += 1

    for i in range(l, r + 1):
        nums[i] = nums_copy[i]
    return count_inf


def search_inversions(nums, nums_copy, l, r):
    if r <= l:
        return 0

    mid = (l + r) // 2
    inversins = 0
    inversins += search_inversions(nums, nums_copy, l, mid)
    inversins += search_inversions(nums, nums_copy, mid + 1, r)
    inversins += search(nums, nums_copy, l, mid, r)

    return inversins

if __name__ == '__main__':
    data = read_from_file('lab2/task3/txtf/input.txt')
    n, array = data[0], data[1:]
    result = search_inversions(array, array, 0, int(n)-1)

    write_in_file('lab2/task3/txtf/output.txt', str(result))

    measuring(search_inversions, array, array, 0, int(n)-1)
