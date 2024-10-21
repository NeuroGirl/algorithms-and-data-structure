import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', '..')
print(src_dir)
sys.path.insert(0, src_dir)

from utils import open_close, write

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


file = open_close(1, 1)
if 1 <= file[0] <= 2 * 10 ** 4:
    f = file[1]
    nums = list(map(int, list(f.split(' '))))
    if all([abs(x) <= 10 ** 9 for x in nums]):
        write(1, ' '.join(map(str, sort_merge(nums))))
    else:
        print('Введите подходящие числа')
else:
    print('Неверное количество введенных чисел')