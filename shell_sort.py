import time
import random


def shell_sort(arr):
    start = time.time()
    n = len(arr)
    gap = n // 2
    comparison = 0
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j - gap >= 0 and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
                comparison += 1
            if j - gap >= 0:
                comparison += 1
            arr[j] = temp
        gap //= 2
    return arr, comparison, time.time() - start


