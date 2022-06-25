

buku = []


def show_data():
    if len(buku) < 1:
        print("Data kosong")
    else:
        for i in range(len(buku)):
            print("{%d} %s" % (i, buku[i]))


def tambah_data():
    buku_baru = input("Judul Buku : ")
    buku.append(buku_baru)
    print("Data berhasil ditambahkan")


def edit_data():
    show_data()
    index = int(input("Inputkan Id Buku : "))

    if(index > len(buku)):
        print("Id tidak ditemukan")
    else:
        judul_baru = input("Judul Buku Baru : ")
        buku[index] = judul_baru


def delete_data():
    show_data()

    index = int(input("Inputkan Id Buku : "))

    if(index > len(buku)):
        print("Id tidak ditemukan")
    else:
        buku.remove(buku[index])
        print("Data berhasil dihapus")


def show_menu():
    print("""
    1. Tampilkan Data
    2. Tambah Data
    3. Edit Data
    4. Hapus Data
    5. Keluar
    """)

    menu = int(input("Pilih menu : "))
    if menu == 1:
        show_data()
    elif menu == 2:
        tambah_data()
    elif menu == 3:
        edit_data()
    elif menu == 4:
        delete_data()
    elif menu == 5:
        exit()
    else:
        print("Menu tidak ada")


if __name__ == "__main__":
    while True:
        show_menu()
