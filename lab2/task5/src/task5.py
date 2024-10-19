def majority_finder(a):
    dic = {}
    for i in a:
        dic[i] = dic.get(i, 0) + 1

    for k, v in dic.items():
        if v > len(a) // 2:
            return 1
    return 0


with open('C:/Users/ВЕРОНИКА/Desktop/показ/lab-aisd/lab2/task5/txtf/output.txt', 'w') as f:
    file = open('C:/Users/ВЕРОНИКА/Desktop/показ/lab-aisd/lab2/task5/txtf/input.txt')
    n = int(file.readline())
    list_input = list(map(int, file.readline().split()))
    f.write(str(majority_finder(list_input)))