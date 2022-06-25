# Soal No 1 - 3
inputUser = int(input("Masukkan Bilangan: "))

# Soal No #1
# Menentukan Bilangan Negatif atau Positif


def positive_or_negative(inputUser):
    # Memeriksa Bilangan Positif atau Negatif
    if inputUser > 0:
        print(f"{inputUser} >..Bilangan Positive..<")
    elif inputUser < 0:
        print(f"{inputUser} >..Bilangan Negative..<")
    else:
        print(f"{inputUser} >..Bilangan 0..<")


# Soal No #2
# Menentukan Bilangan Genap atau Ganjil
def ganjil_genap(inputUser):
    # Memeriksa Bilangan Ganjil atau Genap
    if inputUser % 2 == 0:
        print(f"{inputUser} >..Bilangan Genap..<")
    else:
        print(f"{inputUser} >..Bilangan Ganjil..<")


# Soal No #3
# Menentukan Bilangan Prima atau Bukan Prima
def prima(inputUser):
    if inputUser > 1:
        # Memeriksa Bilangan Prima atau Bukan Prima
        for i in range(2, inputUser):
            if inputUser % i == 0:
                print(f"{inputUser} >..Bukan Bilangan Prima..<")
                break
        else:
            print(f"{inputUser} >..Bilangan Prima..<")
    else:
        print(f"{inputUser} >..Bilangan Prima..<")


# Memanggil Fungsi
positive_or_negative(inputUser)
ganjil_genap(inputUser)
prima(inputUser)
