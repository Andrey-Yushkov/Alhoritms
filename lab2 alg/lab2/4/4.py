import time, psutil, random
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

with open("input.txt", "r") as file:
    n1 = int(file.readline())
    a = [int(i) for i in file.readline().split()]
    n2 = int(file.readline())
    b = [int(i) for i in file.readline().split()]
c = []
for i in range(len(b)):
    c.append(binary_search(a, b[i]))
ans = str(c[0])
for i in range(len(c) - 1):
    ans = ans + ' ' +  str(c[i + 1])
with open("output.txt", "w") as file:
    file.write(ans)
print("Время работы: %s секунд " % (time.perf_counter() - t_start))
print('Памяти использовано', psutil.Process().memory_info().rss/1024**2, "МБ")