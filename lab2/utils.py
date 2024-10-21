def open_close(n, k):
    input_f = open(f"C:/Users/ВЕРОНИКА/Desktop/показ/lab-aisd/lab2/task{n}/txtf/input.txt")
    res = []
    if k == -1:
        res.append(input_f.readline())
    elif k == -2:
        res.append(int(input_f.readline()))
        res.append(input_f.readline())
        res.append(input_f.readline())
    else:
        for _ in range(k):
            res.append(int(input_f.readline()))
            res.append(input_f.readline())
        input_f.close()
    return res

def write(n, result):
    output_f = open(f"C:/Users/ВЕРОНИКА/Desktop/показ/lab-aisd/lab2/task{n}/txtf/output.txt", 'w')
    output_f.write(result)
    output_f.close()