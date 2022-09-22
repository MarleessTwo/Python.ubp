from memory_profiler import profile


import time
#


@profile
def my_func():
    startTime = time.time()

    for i in range(1, 10):
        i += 1
        print(i)

    endTime = time.time()
    print()
    print("Duration : ", endTime - startTime)


if __name__ == '__main__':
    my_func()
