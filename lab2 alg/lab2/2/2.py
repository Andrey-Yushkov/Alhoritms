import time, psutil, random
from lab2.utils import inp, out
t_start = time.perf_counter()

def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    merged = merge(left, right)
    print("Слияние:", left, right)
    print("Значение:", merged)
    return merged

n, a = inp(2)
a = merge_sort(a)
ans = str(a[0])
for i in range(n - 1):
    ans = ans + ' ' +  str(a[i + 1])
out(ans)
for i in range(3):
    array_size = 11
    random_array = [random.randint(1, 100) for _ in range(array_size)]
    print(f"Массив случайных чисел: {random_array}")
    random_array = merge_sort(random_array)
    print("Отсортированный массив:", random_array)
print("Время работы: %s секунд " % (time.perf_counter() - t_start))
print('Памяти использовано', psutil.Process().memory_info().rss/1024**2, "МБ")