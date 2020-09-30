import copy
import random
import selection_sort
import insertion_sort
import merge_sort
import shell_sort
import matplotlib.pyplot as plt
import numpy as np


def save_graphic(save_name, data, name, yname, xname):
    global START, FINISH
    fig, ax = plt.subplots()
    dim = FINISH - START + 1
    w = 0.2 * dim
    dimw = w / dim
    x = np.arange(dim)
    k = 0
    for i in data[2 ** START]:
        y = []
        now = 2 ** START
        while now <= 2 ** FINISH:
            y.append(data[now][i])
            now *= 2
        y = np.array(y)
        print(x)
        b = ax.bar(x + k * dimw, y, dimw, bottom=0.001)
        k += 1
    ax.set_xticks(x + 3 * dimw / 2)
    ax.set_xticklabels(['2**' + str(x) for x in range(START, FINISH + 1)])
    ax.set_yscale('log')
    ax.set_xlabel(xname)
    ax.set_ylabel(yname)
    plt.title(name)
    plt.savefig(save_name)
    plt.clf()

START,FINISH = 7,15 # Початковий і кінцевий розмір масиву 2**
now = 2 ** START
answers_comparison,answers_time = {},{}
while now <= 2 ** FINISH:
    answers_comparison[now] = {
        'selection_sort': 0,
        'insertion_sort': 0,
        'merge_sort': 0,
        'shell_sort': 0
    }
    answers_time[now] = copy.copy(answers_comparison[now])

    kk = 5 # Кількість експериментів
    for i in range(kk):
        arr = random.choices(range(now),k=now)
        arr_selection_sort, comparison_selection_sort, time_selection_sort = selection_sort.selection_sort(
            copy.copy(arr))
        arr_insertion_sort, comparison_insertion_sort, time_insertion_sort = insertion_sort.insertion_sort(
            copy.copy(arr))
        arr_merge_sort, comparison_merge_sort, time_merge_sort = merge_sort.merge_sort(copy.copy(arr))
        arr_shell_sort, comparison_shell_sort, time_shell_sort = shell_sort.shell_sort(copy.copy(arr))
        answers_comparison[now]['selection_sort'] += comparison_selection_sort / kk
        answers_time[now]['selection_sort'] += time_selection_sort / kk
        answers_comparison[now]['insertion_sort'] += comparison_insertion_sort / kk
        answers_time[now]['insertion_sort'] += time_insertion_sort / kk
        answers_comparison[now]['merge_sort'] += comparison_merge_sort / kk
        answers_time[now]['merge_sort'] += time_merge_sort / kk
        answers_comparison[now]['shell_sort'] += comparison_shell_sort / kk
        answers_time[now]['shell_sort'] += time_shell_sort / kk
    now *= 2

save_graphic('Time_randem', answers_time,
             'Average time complexity for different sorting algorithms', 'Time Complexity', 'Size of an array')
save_graphic('Comparison_randem', answers_comparison,
             'Average number of comparison for different sorting algorithms', 'Number of comparison', 'Size of an array')
