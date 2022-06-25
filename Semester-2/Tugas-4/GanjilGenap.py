# Soal No #5
# Menentukan Bilangan Genap atau Ganjil


def ganjil_genap(n):
    if n % 2 == 0:
        print(f"{n} >..Bilangan Genap..<")
    else:
        print(f"{n} >..Bilangan Ganjil..<")


def main():
    ganjil_genap(3)


if __name__ == "__main__":
    main()
