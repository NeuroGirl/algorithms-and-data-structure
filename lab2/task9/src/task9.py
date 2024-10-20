def read(num_len, file_A, file_B):
    a = []
    b = []
    d = []
    for x in file_A:
        d.append(int(x))
        if len(d) == num_len:
            a.append(d) 
            d = []
    for x in file_B:
        d.append(int(x))
        if len(d) == num_len:
            b.append(d) 
            d = []
    return [a, b]

def divide(num_len, file_A, file_B):
    g = read(num_len, file_A, file_B)
    new_a= []
    for a in g[0]:
        if len(a) > 2:
            d = []
            for x in a:
                d.append(x)
                if len(d) == 2:
                    new_a.append(d)
                    d = []
        else:
            continue
    if new_a == []:
        new_a = g[0].copy()

    new_b= []
    for b in g[1]:
        if len(b) > 2:
            d = []
            for x in b:
                d.append(x)
                if len(d) == 2:
                    new_b.append(d)
                    d = []
        else:
            continue
    if new_b == []:
        new_b = g[1].copy()

    return [new_a, new_b]

def block_merge(num_len, file_A, file_B):
    g = divide(num_len, file_A, file_B)
    a = g[0]
    new_a = []
    row = []
    x = 0
    while x != len(a):
        row.append([a[x], a[x + num_len // 2]])
        if len(row) == num_len // 2:
            new_a.append(row)
            row = []
            x += num_len // 2
        x += 1

    b = g[1]
    new_b = []
    row = []
    x = 0
    while x != len(b):
        row.append([b[x], b[x + num_len // 2]])
        if len(row) == num_len // 2:
            new_b.append(row)
            row = []
            x += num_len // 2
        x += 1
    return [new_a, new_b]

def strassen(file_A, file_B):
    mat_a = file_A
    mat_b = file_B
    p1 = mat_a[0][0] * (mat_b[0][1] - mat_b[1][1])
    p2 = (mat_a[0][0] + mat_a[0][1]) * mat_b[1][1]
    p3 = (mat_a[1][0] + mat_a[1][1]) * mat_b[0][0]
    p4 = mat_a[1][1] * (mat_b[1][0] - mat_b[0][0])
    p5 = (mat_a[0][0] + mat_a[1][1]) * (mat_b[0][0] + mat_b[1][1])
    p6 = (mat_a[0][1] - mat_a[1][1]) * (mat_b[1][0] + mat_b[1][1])
    p7 = (mat_a[0][0] - mat_a[1][0]) * (mat_b[0][0] + mat_b[0][1])
    c = []
    c.append([p5 + p4 - p2 + p6, p1 + p2])
    c.append([p3 + p4, p1 + p5 - p3 - p7])
    return c

def strassen_apply(num_len, file_A, file_B):
    g = block_merge(num_len, file_A, file_B)
    a = g[0]
    b = g[1]
    final = []
    for x in range(len(a)):
        row_a = a[x]
        row_b = b[x]
        for y in range(len(row_a)):
            st_a = row_a[y]
            st_b = row_b[y]
            c = strassen(st_a, st_b)
            final.append(c)
    return(final)
 
output_f = open("C:/Users/ВЕРОНИКА/Desktop/показ/lab-aisd/lab2/task9/txtf/output.txt", 'w')
input_f = open("C:/Users/ВЕРОНИКА/Desktop/показ/lab-aisd/lab2/task9/txtf/input.txt")
num_len = int(input_f.readline())
g = input_f.readline()
h = input_f.readline()
file_A = list(map(int, list(g.split(' '))))
file_B = list(map(int, list(h.split(' '))))

output_f.write(' '.join(map(str, strassen_apply(num_len, file_A, file_B))))

output_f.close()
input_f.close()