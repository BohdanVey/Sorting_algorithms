import shell_sort
import random
import copy


def shell_sort2(lst):
    n = len(lst)
    # Initial step
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            # Insert sorting for each step
            temp = lst[i]
            j = i
            # Insertion sort
            while j >= 0 and j - gap >= 0 and lst[j - gap] > temp:
                lst[j] = lst[j - gap]
                j -= gap
            lst[j] = temp
        # Get the new step
        gap = gap // 2
    return lst
a = random.sample(range(20000000), 100000)
a2 = copy.copy(a)
import time

start = time.time()
a1 = shell_sort2(a)
print(time.time() - start)
start = time.time()
a3 = shell_sort.shell_sort(a2)
print(time.time() - start)
print(a1 == sorted(a1))
