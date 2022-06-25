# Soal No. #10

# (a) 1 - 5 - 2 - 10 - 3 - 15
i = 1
while i <= 3:
    x = 5*i
    print(f"{i} - {x}", end=' ')
    print("-", end=' ')
    i += 1
print("\b\b ")

# (b) 2 - UBP - 4 - UBP - 6 - UBP
i = 1
while i <= 3:
    num = 2*i
    s = "UBP"
    print(f"{num} - {s}", end=' ')
    print("-", end=' ')
    i += 1
print("\b\b ")
