def ForLoop4(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        print(a)

ForLoop4(10)