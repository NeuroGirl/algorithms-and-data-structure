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

output_f = open("C:/Users/ВЕРОНИКА/Desktop/показ/lab-aisd/lab2/task3/txtf/output.txt", 'w')
input_f = open("C:/Users/ВЕРОНИКА/Desktop/показ/lab-aisd/lab2/task3/txtf/input.txt")
num_len = int(input_f.readline())
file = input_f.readline()
if 1 <= num_len <= 10 ** 5:
    nums = list(map(int, list(file.split(' '))))
    nums_copy = nums.copy()
    if all([abs(x) <= 10 ** 9 for x in nums]):
        output_f.write(str(search_inversions(nums, nums_copy, 0, num_len - 1)))
    else:
        print('Введите подходящие числа')
else:
    print('Неверное количество введенных чисел')

output_f.close()
input_f.close()