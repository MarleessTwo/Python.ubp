from memory_profiler import profile
import time
#


@profile
def my_func():
    startTime = time.time()

    number = 1
    if (number <= 10):
        print(number)
        number += 1
    if (number <= 10):
        print(number)
        number += 1
    if (number <= 10):
        print(number)
        number += 1
    if (number <= 10):
        print(number)
        number += 1
    if (number <= 10):
        print(number)
        number += 1
    if (number <= 10):
        print(number)
        number += 1
    if (number <= 10):
        print(number)
        number += 1
    if (number <= 10):
        print(number)
        number += 1
    if (number <= 10):
        print(number)
        number += 1
    if (number <= 10):
        print(number)

    endTime = time.time()
    print()
    print("Duration : ", endTime - startTime)


if __name__ == '__main__':
    my_func()
