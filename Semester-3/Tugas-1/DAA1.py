from memory_profiler import profile
import time


@profile
def my_func():
    startTime = time.time()

    Number = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    print(Number)

    endTime = time.time()
    print('Duration: {}'.format(endTime - startTime))


if __name__ == '__main__':
    my_func()
