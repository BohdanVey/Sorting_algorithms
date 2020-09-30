import time
import random


def insertion_sort(a):
    comparison = 0
    start = time.time()
    n = len(a)
    for i in range(1, n):
        now = a[i]
        l, r = -1, i
        while r - l > 1:
            comparison += 1
            if now >= a[(l + r) // 2]:
                l = (l + r) // 2
            else:
                r = (l + r) // 2
        k = r
        for j in range(i - 1, k - 1, -1):
            a[j + 1] = a[j]
        a[k] = now
    return a, comparison, time.time() - start


