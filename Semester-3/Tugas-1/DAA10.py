from array import array
from memory_profiler import profile
import time
#


@profile
def my_func():
    startTime = time.time()

    array = [10, 7, 9, 4, 5, 1, 3, 2, 6, 8]
    size = len(array)
    sortSelection(array, size)
    print(array)

    endTime = time.time()
    print()
    print("Duration : ", endTime - startTime)


def sortSelection(array, size):
    for i in range(size):
        minIndex = i
        for j in range(i + 1, size):
            if array[j] < array[minIndex]:
                minIndex = j
        array[i], array[minIndex] = array[minIndex], array[i]


if __name__ == '__main__':
    my_func()
