from profile_decorator import ProfileDecorator

@ProfileDecorator
def bubbleSort(arr):
    """
    Сортировка списка методом пузырька.

    param: arr (list): Список для сортировки.

    returns: list: Отсортированный список.
    """
    #arr=_arr.copy()
    n = len(arr)
    if (n>0):
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def bubbleSortMultipleTimes(arr, num_times):
    if (num_times>0):
        for _ in range(num_times):
            sorted_list = bubbleSort(arr)
            stats = bubbleSort.get_stats()
            print(stats)
            bubbleSort.reset_time()
        