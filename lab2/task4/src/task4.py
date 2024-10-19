file = open('C:/Users/ВЕРОНИКА/Desktop/показ/lab-aisd/lab2/task4/txtf/input.txt')
n, mass = int(file.readline()), list(map(int, file.readline().split()))
k, mass_find = int(file.readline()), list(map(int, file.readline().split()))


def bin_searching(mass, what_find):
    l = 0
    r = len(mass) - 1
    while l <= r:
        mid = (l + r) // 2
        if what_find == mass[mid]:
            return mid
        elif what_find < mass[mid]:
            r = mid - 1
        else:
            l = mid + 1
    return -1


def start_search(mass, mass_find):
    return [bin_searching(mass, mass_find[i]) for i in range(len(mass_find))]


output_f = open("C:/Users/ВЕРОНИКА/Desktop/показ/lab-aisd/lab2/task1/txtf/output.txt", 'w')
output_f.write(' '.join(map(str, start_search(mass, mass_find))))