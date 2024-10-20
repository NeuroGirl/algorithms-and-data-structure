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


def strassen(num_len, file_A, file_B):
    g = read(num_len, file_A, file_B)
    mat_a = g[0]
    mat_b = g[1]
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

#def divide(num_len, file_A, file_B):
#    g = read(num_len, file_A, file_B)
 #   new_a
#
 #   for a in g[1]:
 #       if len(a) > 2:
 #           for _ in range(2):
 
output_f = open("C:/Users/ВЕРОНИКА/Desktop/показ/lab-aisd/lab2/task9/txtf/output.txt", 'w')
input_f = open("C:/Users/ВЕРОНИКА/Desktop/показ/lab-aisd/lab2/task9/txtf/input.txt")
num_len = int(input_f.readline())
g = input_f.readline()
h = input_f.readline()
file_A = list(map(int, list(g.split(' '))))
file_B = list(map(int, list(h.split(' '))))

output_f.write(' '.join(map(str, strassen(num_len, file_A, file_B))))

output_f.close()
input_f.close()