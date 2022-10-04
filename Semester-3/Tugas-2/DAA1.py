from memory_profiler import profile
import time


@profile
def my_func():
    startTime = time.time()
    n = 2
    for i in range(10):
        print(n)
        n = n * 5

    endTime = time.time()
    print()
    print("Duration : ", endTime - startTime)


if __name__ == '__main__':
    my_func()
