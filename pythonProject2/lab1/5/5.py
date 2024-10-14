import time, psutil
t_start = time.perf_counter()
with open("input.txt", "r") as file:
    n = int(file.readline())
    a = [int(i) for i in file.readline().split()]
def selection_sort(n, a):
    q = 0
    if 0 >= n or n > 1000:
        q = 1
    for i in range(n):
        if not (-10 ** 9 <= a[i] <= 10 ** 9):
            q = 1
    if q == 1:
        return print('Неправильный ввод')
    else:
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if a[j] < a[min_index]:
                    min_index = j
            a[i], a[min_index] = a[min_index], a[i]
        ans = str(a[0])
        for i in range(n - 1):
            ans = ans + ' ' + str(a[i + 1])
        with open("output.txt", "w") as file:
            file.write(ans)
selection_sort(n, a)
print("Время работы: %s секунд " % (time.perf_counter() - t_start))
print(psutil.Process().memory_info().rss/1024**2)