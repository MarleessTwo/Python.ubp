from memory_profiler import profile
import time


@profile
def my_func():
    startTime = time.time()
    f(20)

    endTime = time.time()
    print()
    print("Duration : ", endTime - startTime)


def f(n):
    for i in range(n):
        n = 2*n**2 + 1
        print(n)


if __name__ == '__main__':
    my_func()
