from memory_profiler import profile
import time
#


@profile
def my_func():
    startTime = time.time()

    number = 10
    number = number / 2 - 4
    print(int(number))
    number = number / 2 + 2

    print(int(number))
    number = number / 2 + 2
    print(int(number))
    number = number / 2 + 3
    print(int(number))
    number = number / 2 + 3
    print(int(number))
    number = number / 2 + 4
    print(int(number))
    number = number / 2 + 4
    print(int(number))
    number = number / 2 + 5
    print(int(number))
    number = number / 2 + 5
    print(int(number))
    number = number / 2 + 6
    print(int(number))

    endTime = time.time()
    print()
    print("Duration : ", endTime - startTime)


if __name__ == '__main__':
    my_func()
