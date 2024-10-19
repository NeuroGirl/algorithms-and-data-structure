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

output_f = open("C:/Users/ВЕРОНИКА/Desktop/показ/lab-aisd/lab2/task1/txtf/output.txt", 'w')
input_f = open("C:/Users/ВЕРОНИКА/Desktop/показ/lab-aisd/lab2/task1/txtf/input.txt")
num_len = int(input_f.readline())
file = input_f.readline()
if 1 <= num_len <= 2 * 10 ** 4:
    nums = list(map(int, list(file.split(' '))))
    if all([abs(x) <= 10 ** 9 for x in nums]):
        output_f.write(' '.join(map(str, sort_merge(nums))))
    else:
        print('Введите подходящие числа')
else:
    print('Неверное количество введенных чисел')

output_f.close()
input_f.close()