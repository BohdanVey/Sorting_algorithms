import time
import random


def selection_sort(a):

    comparison = 0
    start = time.time()
    n = len(a)
    for i in range(n):
        mini = a[i]
        idx = i
        # Знаходимо мінімальний елемент серед тих що залишилися
        for j in range(i + 1, n):
            comparison += 1
            if mini > a[j]:
                idx = j
                mini = a[j]

        a[i], a[idx] = a[idx], a[i]


    return a, comparison, time.time() - start
   # Знаходимо мінімальний елемент серед тих що залишилися(дана операція виконується n раз, на кожному кроці к-сть елементів, що залишилися на один менша ніж на попередньому


