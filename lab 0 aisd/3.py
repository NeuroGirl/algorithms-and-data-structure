import time
t_start = time.perf_counter()
d = open("input.txt")
n = int(d.readline())
a = [0, 1]
for i in range(n-1):
    a.append(a[-1] + a[-2])
if 0 <= n <= 10**7:
    new_f = open("output.txt", "w+")
    new_f.write(f'{a[-1] % 10}')
    new_f.close()
print(time.perf_counter() - t_start)