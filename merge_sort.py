import time
import random


def merge_sort(arr):

    start = time.time()
    if len(arr) == 1:
        return arr, 0,0
    m = len(arr) // 2
    arr1, comparison1, _ = merge_sort(arr[:m])
    arr2, comparison2, _ = merge_sort(arr[m:])
    comparison = comparison1 + comparison2
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        comparison += 1
        if arr1[i] < arr2[j]:
            arr[i + j] = arr1[i]
            i += 1
        else:
            arr[i + j] = arr2[j]
            j += 1
    while i < len(arr1):
        arr[i + j] = arr1[i]
        i += 1
    while j < len(arr2):
        arr[i + j] = arr2[j]
        j += 1
    return arr, comparison, time.time() - start


if __name__ == '__main__':
    print(merge_sort(random.sample(range(10), 10)))
