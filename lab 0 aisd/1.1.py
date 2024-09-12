import time
t_start = time.perf_counter()
nums = input().split(" ")
a = int(nums[0])
b = int(nums[1])
if -10**9 < a < 10**9 and -10**9 < a < 10**9:
    print(a + b)
print(time.perf_counter() - t_start)