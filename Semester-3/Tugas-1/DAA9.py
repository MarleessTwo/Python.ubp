from memory_profiler import profile
import time
#


@profile
def my_func():
    startTime = time.time()

    recursive(1)

    endTime = time.time()
    print()
    print("Duration : ", endTime - startTime)


def recursive(number):
    if number <= 10:
        print(number)
        number += 1
        recursive(number)


if __name__ == '__main__':
    my_func()
