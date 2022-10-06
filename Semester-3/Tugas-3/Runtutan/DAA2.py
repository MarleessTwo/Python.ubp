def runtutan(n):
    if n == 1 or n == 2:
        return 1
    else:
        a = 1
        b = 1
        for i in range(3, n+1):
            c = a + b
            a = b
            b = c
            print(c)
        return b


runtutan(5)
