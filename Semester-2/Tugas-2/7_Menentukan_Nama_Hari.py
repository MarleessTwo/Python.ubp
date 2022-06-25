# Soal No #7
# Menentukan Nama Hari Dalam Seminggu
inputUser = int(input("Masukan Nomor 1 - 7 Dalam Hari: "))


def switch(case):
    print(
        f"Hari ke {inputUser} Adalah Hari ")
    if case == 1:
        print("Senin")

    elif case == 2:
        print("Selasa")

    elif case == 3:
        print("Rabu")

    elif case == 4:
        print("Kamis")

    elif case == 5:
        print("Jumat")

    elif case == 6:
        print("Sabtu")

    elif case == 7:
        print("Minggu")

    else:
        print("Mohon Masukan Nomor 1-7")


# Memanggil Fungsi Switch
switch(inputUser)
