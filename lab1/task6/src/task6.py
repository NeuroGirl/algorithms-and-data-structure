def bubble_sort(num_len, list_to_sort):
    for i in range(num_len - 1):
        for j in range(num_len - 1 - i):
            if list_to_sort[j] > list_to_sort[j + 1]:
                list_to_sort[j], list_to_sort[j + 1] = list_to_sort[j + 1], list_to_sort[j]
    return list_to_sort

output_f = open("C:/Users/ВЕРОНИКА/Desktop/показ/lab-aisd/lab1/task6/txtf/output.txt", 'w')
input_f = open("C:/Users/ВЕРОНИКА/Desktop/показ/lab-aisd/lab1/task6/txtf/input.txt")
num_len = int(input_f.readline())
file = input_f.readline()
if 1 <= num_len <= 10 ** 3:
    nums = list(map(int, list(file.split(' '))))
    if all([abs(x) <= 10 ** 9 for x in nums]):
        output_f.write(' '.join(map(str, bubble_sort(num_len, nums))))
    else:
        print('Введите подходящие числа')
else:
    print('Неверное количество введенных чисел')

output_f.close()
input_f.close()