d = open("input.txt")
n = int(d.readline())
a = [0, 1]

while not(0 <= n <= 45):
    print("Неверные входные данные")
    time.sleep(4)
    d = open("input.txt")
    n = int(d.readline())

if 0 <= n <= 45:
    for i in range(n):
        a.append(a[-1] + a[-2])
    new_f = open("output.txt", "w+")
    new_f.write(f'{a[-2]}')
    new_f.close()
d.close()
