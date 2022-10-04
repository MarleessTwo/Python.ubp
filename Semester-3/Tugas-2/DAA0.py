from memory_profiler import profile
import time


@profile
def my_func():
    startTime = time.time()

    array = [
        213, 886, 552, 660, 226,
        684, 168, 190, 719, 722]
    size = len(array)

    for i in range(size):
        minIndex = i
        for j in range(i + 1, size):
            if array[j] < array[minIndex]:
                minIndex = j
                x = array[minIndex]
                array[minIndex] = array[i]
                array[i] = x

    print("Minimum", array[0], "Maximum", array[size-1])

    endTime = time.time()
    print()
    print("Duration : ", endTime - startTime)


if __name__ == '__main__':
    my_func()
