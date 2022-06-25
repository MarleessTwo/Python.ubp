def newLine():
    print("\n")


def Greetings(name):
    print("Hello", name)


def ForLoop(n):
    newLine()
    for i in range(n):
        print(i, end="")


def ForLoop2(a, b, c):
    newLine()
    for i in range(a, b, c):
        print("i = ", i)


def ForLoop3():
    newLine()
    namaBuah = 'Mangga', 'Jeruk', 'Apel', 'Pisang'
    for buah in namaBuah:
        print(buah)


def ForLoop4(n):
    newLine()
    for i in range(n):
        print(f"Perulangan ke-{i}")


def WhileLoop(n):
    newLine()
    i = 0
    while i < n:
        i = i + 2
        print(i, end="*")


if __name__ == "__main__":
    Greetings('Bangsat')
    ForLoop(11)
    # (2 -> "Batas Awal", 12 -> "Batas Akhir", 2 -> "Kelipatan")
    ForLoop2(2, 12, 2)
    ForLoop3()
    ForLoop4(11)
    WhileLoop(10)
