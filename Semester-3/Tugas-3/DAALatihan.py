
def bilangan(n):
    if n == 1:
        return 1
    else:
        return 2*n + bilangan(n-1)


print(bilangan(6))

#  1 + 2*2 + 2*3 + 2*4 + 2*5 + 2*6
#  1 + 4 + 6 + 8 + 10 + 12
#  41
