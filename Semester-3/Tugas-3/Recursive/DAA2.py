# Fibonacci Recursive

def recursive(n):

    if n < 2:
        return n

    else:
        return recursive(n-1) + recursive(n-2)


print(recursive(6))
