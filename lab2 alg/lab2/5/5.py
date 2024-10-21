import time, psutil
from lab2.utils import inp, out
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

n, a = inp(2)
if majority_element(a):
    out('1')
else:
    out('0')
print("Время работы: %s секунд " % (time.perf_counter() - t_start))
print('Памяти использовано', psutil.Process().memory_info().rss/1024**2, "МБ")