from memory_profiler import profile
import time


@profile
def my_func():
    startTime = time.time()

    number = 1
    print(number)
    number = number + 1
    print(number)
    number = number + 1
    print(number)
    number = number + 1
    print(number)
    number = number + 1
    print(number)
    number = number + 1
    print(number)
    number = number + 1
    print(number)
    number = number + 1
    print(number)
    number = number + 1
    print(number)
    number = number + 1
    print(number)

    endTime = time.time()
    print('Duration: {}'.format(endTime - startTime))


if __name__ == '__main__':
    my_func()
