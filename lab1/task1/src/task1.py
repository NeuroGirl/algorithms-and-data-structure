output_f = open("C:/Users/ВЕРОНИКА/Desktop/показ/lab-aisd/lab1/task1/txtf/output.txt", 'w')

def insertion_sort(num_len, list_to_sort):
    for i in range(1, num_len):
        key = list_to_sort[i]
        j = i - 1
        while j >= 0 and key < list_to_sort[j]:
            list_to_sort[j + 1] = list_to_sort[j]
            j -= 1
        list_to_sort[j + 1] = key
    return list_to_sort


input_f = open("C:/Users/ВЕРОНИКА/Desktop/показ/lab-aisd/lab1/task1/txtf/input.txt")
num_len = int(input_f.readline())
file = input_f.readline()
if 1 <= num_len <= 10 ** 3:
    nums = list(map(int, list(file.split(' '))))
    if all([abs(x) <= 10 ** 9 for x in nums]):
        output_f.write(' '.join(map(str, insertion_sort(num_len, nums))))
    else:
        print('Введите подходящие числа')
else:
    print('Неверное количество введенных чисел')

output_f.close()
input_f.close()