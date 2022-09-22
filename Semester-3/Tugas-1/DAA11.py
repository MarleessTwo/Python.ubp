from memory_profiler import profile
import time
#


@profile
def my_func():
    startTime = time.time()

    print(quicksort(0, len(array)-1, array))

    endTime = time.time()
    print("Duration : ", endTime - startTime)


array = [10, 7, 9, 4, 5, 1, 3, 2, 6, 8]


def partition(low, high, array):
    i = low-1
    pivot = array[high]
    for j in range(low, high):
        if array[j] <= pivot:
            i = i+1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[high] = array[high], array[i+1]
    return (i+1)


def quicksort(low, high, array):
    if low < high:
        pi = partition(low, high, array)
        quicksort(low, pi-1, array)
        quicksort(pi+1, high, array)
    return array


if __name__ == '__main__':
    my_func()
