import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', '..')
print(src_dir)
sys.path.insert(0, src_dir)

from utils import open_close, write

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

file = open_close(3, 1)
if 1 <= file[0] <= 10 ** 5:
    f = file[1]
    nums = list(map(int, list(f.split(' '))))
    nums_copy = nums.copy()
    if all([abs(x) <= 10 ** 9 for x in nums]):
        write(3, str(search_inversions(nums, nums_copy, 0, file[0] - 1)))
    else:
        print('Введите подходящие числа')
else:
    print('Неверное количество введенных чисел')