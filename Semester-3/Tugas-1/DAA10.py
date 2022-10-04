from memory_profiler import profile
import time
#


@profile
def my_func():
    startTime = time.time()

    array = [100, 71, 29, 14, 555, 11, 63, 12, 36, 89]
    size = len(array)
    sortSelection(array, size)
    print("Minimum", array[0], "Maximum", array[size-1])

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
