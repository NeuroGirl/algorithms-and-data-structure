output_f = open("C:/Users/ВЕРОНИКА/Desktop/показ/lab-aisd/lab1/task2/txtf/output.txt", 'w')

def insertion_sort_advanced(num_len, list_to_sort):
    motions = [1]
    for i in range(1, num_len):
        for j in range(i - 1, -1, -1):
            if list_to_sort[i] < list_to_sort[j]:
                list_to_sort[i], list_to_sort[j] = list_to_sort[j], list_to_sort[i]
                i, j = j, i
        motions.append(i + 1)
    return motions, list_to_sort


input_f = open("C:/Users/ВЕРОНИКА/Desktop/показ/lab-aisd/lab1/task2/txtf/input.txt")
num_len = int(input_f.readline())
file = input_f.readline()
if 1 <= num_len <= 10 ** 3:
    nums = list(map(int, list(file.split(' '))))
    if all([abs(x) <= 10 ** 9 for x in nums]):
        motion_list, sorted_list = insertion_sort_advanced(num_len, nums)
        output_f.write(f"{' '.join(map(str, motion_list))}\n")
        output_f.write(' '.join(map(str, sorted_list)))
    else:
        print('Введите подходящие числа')
else:
    print('Неверное количество введенных чисел')

output_f.close()
input_f.close()