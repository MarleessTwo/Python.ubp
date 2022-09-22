from memory_profiler import profile
import time
#


@profile
def my_func():
    startTime = time.time()

    numberA = 1
    numberB = 2
    numberC = 3
    numberD = 4
    numberE = 5
    numberF = 6
    numberG = 7
    numberH = 8
    numberI = 9
    numberJ = 10

    print(numberA,
          numberB, numberC,
          numberD, numberE,
          numberF, numberG,
          numberH, numberI, numberJ)

    endTime = time.time()
    print()
    print("Duration : ", endTime - startTime)


if __name__ == '__main__':
    my_func()
