f = open("input.txt")
nums = f.readline().split(" ")
a = int(nums[0])
b = int(nums[1])
if -10**9 <= a <= 10**9 and -10**9 <= a <= 10**9:
    new_f = open("output.txt", "w+")
    new_f.write(f'{a + b}')
    new_f.close()
f.close()
