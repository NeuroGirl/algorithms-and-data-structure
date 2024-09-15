d = open("input.txt")
n = int(d.readline())
f1 = 0
f2 = 1
temp = 0
if 0 < n <= 10**7:
    for i in range(n-1):
        temp = f1 % 10
        f1 = f2 % 10
        f2 = (f1 + temp) % 10
    new_f = open("output.txt", "w+")
    new_f.write(f'{f2}')
elif n == 0:
    new_f = open("output.txt", "w+")
    new_f.write(f'{f1}')
new_f.close()
d.close()
