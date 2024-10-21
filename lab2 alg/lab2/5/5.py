import time, psutil, random
t_start = time.perf_counter()
def majority_element(nums):
    candidate = None
    count = 0
    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
    if candidate is not None and nums.count(candidate) > len(nums) // 2:
        return True
    else:
        return False

with open("input.txt", "r") as file:
    n = int(file.readline())
    a = [int(i) for i in file.readline().split()]
if majority_element(a):
    with open("output.txt", "w") as file:
        file.write('1')
else:
    with open("output.txt", "w") as file:
        file.write('0')
print("Время работы: %s секунд " % (time.perf_counter() - t_start))
print('Памяти использовано', psutil.Process().memory_info().rss/1024**2, "МБ")