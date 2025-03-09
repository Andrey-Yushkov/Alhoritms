from lab3.utils import *
from lab3.task1.src.task1 import random_quick_sort

def sort_dolls(dolls_number, hand, dolls):
    groups = [[] for _ in range(hand)]

    for i in range(dolls_number):
        groups[i % hand].append(dolls[i])

    for group in groups:
        random_quick_sort(group)

    sorted_dolls = []
    index = [0] * hand

    for i in range(dolls_number):
        group_index = i % hand
        sorted_dolls.append(groups[group_index][index[group_index]])
        index[group_index] += 1

    if sorted_dolls == random_quick_sort(dolls):
        return "YES"
    return "NO"


def scarecrow_sort():
    (n, k), array = file_read()
    result = sort_dolls(n, k, array)
    file_write([result])


if __name__ == '__main__':
    measure(scarecrow_sort)