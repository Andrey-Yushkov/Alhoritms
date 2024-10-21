import time, psutil
from lab2.utils import inp, out
t_start = time.perf_counter()
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

n1, a, n2, b = inp(4)
c = []
for i in range(len(b)):
    c.append(binary_search(a, b[i]))
ans = str(c[0])
for i in range(len(c) - 1):
    ans = ans + ' ' +  str(c[i + 1])
out(ans)
print("Время работы: %s секунд " % (time.perf_counter() - t_start))
print('Памяти использовано', psutil.Process().memory_info().rss/1024**2, "МБ")