from memory_profiler import profile
from datetime import datetime


@profile
def my_func():
    startTime = datetime.now()

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

    endTime = datetime.now()
    print('Duration: {}'.format(endTime - startTime))


if __name__ == '__main__':
    my_func()
