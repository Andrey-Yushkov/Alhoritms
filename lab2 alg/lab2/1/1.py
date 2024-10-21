import time, psutil, random
t_start = time.perf_counter()

def merge_sort(a):
    if len(a) > 1:
        mid = len(a) // 2
        left_half = a[:mid]
        right_half = a[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                a[k] = left_half[i]
                i += 1
            else:
                a[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            a[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            a[k] = right_half[j]
            j += 1
            k += 1
with open("input.txt", "r") as file:
    n = int(file.readline())
    arr = [int(i) for i in file.readline().split()]
merge_sort(arr)
ans = str(arr[0])
for i in range(n - 1):
    ans = ans + ' ' +  str(arr[i + 1])
with open("output.txt", "w") as file:
    file.write(ans)
for i in range(3):
    array_size = 10
    random_array = [random.randint(1, 100) for _ in range(array_size)]
    print(f"Массив случайных чисел: {random_array}")
    merge_sort(random_array)
    print("Отсортированный массив:", random_array)
print("Время работы: %s секунд " % (time.perf_counter() - t_start))
print('Памяти использовано', psutil.Process().memory_info().rss/1024**2, "МБ")