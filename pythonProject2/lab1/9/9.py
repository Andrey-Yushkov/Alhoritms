import time, psutil
t_start = time.perf_counter()
with open('input.txt', 'r') as file:
    input_string = file.readline().strip()
a, b = map(str, input_string.split())
def sum(a, b):
    if len(a) != len(b) or len(a) > 1000:
        return print('Неправильный ввод')
    else:
        n = len(a)
        c = [0] * (n + 1)
        flag = 0
        for i in range(n - 1, -1, -1):
            s = int(a[i]) + int(b[i]) + flag
            c[i + 1] = s % 2
            flag = s // 2
        c[0] = flag
        ans = str(c[0])
        for i in range(n):
            ans = ans + str(c[i + 1])
        with open("output.txt", "w") as file:
            file.write(ans)
sum(a, b)
print("Время работы: %s секунд " % (time.perf_counter() - t_start))
print(psutil.Process().memory_info().rss/1024**2)