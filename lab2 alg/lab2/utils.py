def inp(x):
    if x == 2:
        with open("input.txt", "r") as file:
            n = int(file.readline())
            a = [int(i) for i in file.readline().split()]
            return n, a
    else:
        with open("input.txt", "r") as file:
            n1 = int(file.readline())
            a = [int(i) for i in file.readline().split()]
            n2 = int(file.readline())
            b = [int(i) for i in file.readline().split()]
            return n1, a, n2, b
def out(a):
    with open("output.txt", "w") as file:
        file.write(a)
        file.close()