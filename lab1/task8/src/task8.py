def swap_sort(num_len, list_to_sort):
    swaps=[]
    for i in range(num_len - 1):
        k = i + 1
        min_list = list_to_sort[k]
        for j in range(i + 1, num_len):
            if list_to_sort[j] < min_list:
                min_list = list_to_sort[j]
                k = j
        if min_list < list_to_sort[i]:
            list_to_sort[i], list_to_sort[k] = list_to_sort[k], list_to_sort[i]
            swaps.append([i+1,k+1])
    return swaps

output_f = open("C:/Users/ВЕРОНИКА/Desktop/показ/lab-aisd/lab1/task8/txtf/output.txt", 'w')
input_f = open("C:/Users/ВЕРОНИКА/Desktop/показ/lab-aisd/lab1/task8/txtf/input.txt")
num_len = int(input_f.readline())
file = list(map(int, input_f.readline().split()))
if 3 <= num_len <= 5000 and min(file)>=-10**9 and max(file)<=10**9:
    swap_vector = swap_sort(num_len, file)
    for [x, y] in swap_vector:
        output_f.write(f"Swap elements at indices {x} and {y}.\n")
    output_f.write("No more swaps needed.")
else:
    print('Введите подходящие числа в подходящем количестве')

output_f.close()
input_f.close()