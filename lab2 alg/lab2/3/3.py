import time, psutil
from lab2.utils import inp, out
t_start = time.perf_counter()
def merge_count(arr, temp_arr, left, mid, right):
    i = left
    j = mid + 1
    k = left
    inv_count = 0
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)
            j += 1
        k += 1
    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1
    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1
    for i in range(left, right + 1):
        arr[i] = temp_arr[i]
    return inv_count
def merge_sort(arr, temp_arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2
        inv_count += merge_sort(arr, temp_arr, left, mid)
        inv_count += merge_sort(arr, temp_arr, mid + 1, right)
        inv_count += merge_count(arr, temp_arr, left, mid, right)
    return inv_count
n, a = inp(2)
temp_array = [0] * n
result = merge_sort(a, temp_array, 0, n - 1)
out(str(result))
print("Время работы: %s секунд " % (time.perf_counter() - t_start))
print('Памяти использовано', psutil.Process().memory_info().rss/1024**2, "МБ")