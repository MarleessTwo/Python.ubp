
def factorial(n):
    if n == 1:
        return 1
    else:
        return 2 * n + factorial(n-1)


print(factorial(8))


#  1 + 2*2 + 2*3 + 2*4 + 2*5 + 2*6 + 2*7 + 2*8
#  1 + 4 + 6 + 8 + 10 + 12 + 14 + 16
#  41
