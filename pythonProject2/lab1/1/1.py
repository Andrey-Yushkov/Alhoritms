import time, psutil
t_start = time.perf_counter()
with open("input.txt", "r") as file:
    n = int(file.readline())
    a = [int(i) for i in file.readline().split()]
def sort(a, n):
    q = 0
    if 0 >= n or n > 1000:
        q = 1
    for i in range(n):
        if not(-10**9<=a[i] <= 10**9):
            q = 1
    if q == 1:
        return print('Неправильный ввод')
    else:
        for i in range(1, n):
                x = a[i]
                j = i
                while j > 0 and a[j - 1] > x:
                    a[j] = a[j - 1]
                    j -= 1
                a[j] = x
        ans = str(a[0])
        for i in range (n-1):
            ans = ans + ' ' + str(a[i+1])
        with open("output.txt", "w") as file:
            file.write(ans)
sort(a, n)
print("Время работы: %s секунд " % (time.perf_counter() - t_start))
print(psutil.Process().memory_info().rss/1024**2)
