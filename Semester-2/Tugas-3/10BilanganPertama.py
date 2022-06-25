def NewLine():
    print("\n")


# Soal No. #1
# Menampilkna Angka Urut Secara Menurun dari 10 - 1
def ForLoop(n):
    for i in range(n, 0, -1):
        print(i)


# Soal No. #2
# Menampilkan 10 Bilangan Ganjil Pertama
def ForLoop1():
    NewLine()
    for i in range(1, 20, 2):
        print(i)


# Soal No. #3
# Menampilkan 10 Bilangan Genap Pertama
def ForLoop2():
    NewLine()
    for i in range(0, 20, 2):
        print(i)


# Soal No. #4
# Menampilkan 10 Bilangan Kelipatan 5 Pertama
def ForLoop3():
    NewLine()
    for i in range(0, 55, 5):
        print(i)


# Soal No. #5
# Menampilkan 10 Bilangan Prima
def WhileLoop(n):
    NewLine()

    if n > 0 and n <= 10:
        if n == 1 or n == 2:
            x = n+2
        elif n > 2 and n <= 10:
            if n == 10:
                x = (n)*3
            else:
                x = (n-1)*3
    elif n > 10 and n <= 20:
        if n == 13 or n == 14:
            x = (n*3)+3
        else:
            x = (n-2)*4
    else:
        x = 0
    nomor = 0
    for prima in range(2, x):
        VarPrima = prima
        i = 2
        z = 0
        while i <= (VarPrima/2):
            if VarPrima % i == 0:
                z += 1
                break
            i += 1
        if z == 0 and prima != 1:
            nomor += 1
            print(f"{nomor} -> {prima}")


# Soal No. #6
# Menampilkan 10 Bilangan Fibonacci Pertama
def ForLoop4(n):
    NewLine()
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        print(a)


# Soal No. #7
# Menampilkan Teks "UBP Karawang" Sebanyak 10 Kali


def Cetak():
    NewLine()
    for i in range(1, 11):
        print(i, " UBP Karawang")


if __name__ == "__main__":
    ForLoop(10)
    ForLoop1()
    ForLoop2()
    ForLoop3()
    WhileLoop(10)
    ForLoop4(10)
    Cetak()
