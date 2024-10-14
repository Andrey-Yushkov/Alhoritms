import time, psutil
t_start = time.perf_counter()
with open("input.txt", "r") as file:
    n = int(file.readline())
    a = [float(i) for i in file.readline().split()]
def bubble_sort(n, a):
    q = 0
    if n % 2 != 1 or n > 9999:
        q = 1
    for i in range(n):
        if not (-10 ** 6 <= a[i] <= 10 ** 6):
            q = 1
    if q == 1:
        return print('Неправильный ввод')
    else:
        for i in range(n):
            for j in range(0, n - i - 1):
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
        ans = str(a[0]) + ' ' + str(a[n // 2]) + ' ' + str(a[-1])
        with open("output.txt", "w") as file:
            file.write(ans)

bubble_sort(n, a)
print("Время работы: %s секунд " % (time.perf_counter() - t_start))
print(psutil.Process().memory_info().rss/1024**2)