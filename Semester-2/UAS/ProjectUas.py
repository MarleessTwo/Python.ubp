# Project Pemrograman Dasar Praktikum #
# Membuat Aplikasi Traveler

from colorama import Fore
import os

# Kolom Kode Paket
kolom_kode_paket = ["01", "02", "03", "04"]
kolom_rute_perjalanan = ["Karawang - Pantai Pakis Jaya", "Karawang - Curug Cigentis - Gunung Sangga Buana",
                         "Karawang - Candi Jiwa", "Karawang - Pantai Samudra", ]
kolom_min_peserta = ["6 Orang", "6 Orang", "4 Orang", "5 Orang"]
kolom_tarif_perjalanan_str = ["Rp. 1.000.000",
                              "Rp. 500.000", "Rp. 600.000", "Rp. 850.000"]
kolom_tarif_perjalanan_int = [1_000_000, 500_000, 600_000, 850_000]

# Kolom Kode Tambahan
kolom_paket_tambahan = ["A", "B", "C"]
kolom_fasilitas = ["Penginapan", "Penjemputan", "Kuliner"]
kolom_tarif_tambahan_str = ["Rp. 600.000", "Rp. 300.000", "Rp. 300.000"]
kolom_tarif_tambahan_int = [600_000, 300_000, 300_000]

# Fungsi List Menu Kode Paket
def show_kode_paket_perjalanan():

    print("}"f"{Fore.RED}------------------------------{Fore.RESET}{Fore.GREEN} DAFTAR KODE PAKET {Fore.RESET}{Fore.RED}------------------------------{Fore.RESET}""{")
    print(f"\n{Fore.GREEN}[{Fore.RESET} {Fore.YELLOW}KODE{Fore.RESET} {Fore.GREEN}]{Fore.RESET} RUTE PERJALANAN {Fore.YELLOW}/{Fore.RESET} MINIMUM PESERTA {Fore.YELLOW}/{Fore.RESET} TARIF\n")
    for pilihan_paket_tujuan in range(len(kolom_kode_paket)):
        print(f"{Fore.GREEN}[{Fore.RESET}  {Fore.YELLOW}{(kolom_kode_paket)[pilihan_paket_tujuan]}{Fore.RESET}  {Fore.GREEN}]{Fore.RESET} {(kolom_rute_perjalanan)[pilihan_paket_tujuan]} {Fore.YELLOW}/{Fore.RESET} {(kolom_min_peserta)[pilihan_paket_tujuan]} {Fore.YELLOW}/{Fore.RESET} {(kolom_tarif_perjalanan_str)[pilihan_paket_tujuan]}")


# Fungsi List Menu Kode Tambahan
def show_fasilitas_tambahan():

    print("\n}"f"{Fore.RED}-----{Fore.RESET}{Fore.GREEN} DAFTAR KODE TAMBAHAN {Fore.RESET}{Fore.RED}-----{Fore.RESET}""{")
    print(
        f"\n{Fore.GREEN}[{Fore.RESET} {Fore.YELLOW}KODE{Fore.RESET} {Fore.GREEN}]{Fore.RESET} FASILITAS {Fore.YELLOW}/{Fore.RESET} TARIF\n")
    for pilihan_fasilitas_tambahan in range(len(kolom_paket_tambahan)):
        print(f"{Fore.GREEN}[{Fore.RESET}  {Fore.YELLOW}{kolom_paket_tambahan[pilihan_fasilitas_tambahan]}{Fore.RESET}   {Fore.GREEN}]{Fore.RESET} {kolom_fasilitas[pilihan_fasilitas_tambahan]} {Fore.YELLOW}/{Fore.RESET} {kolom_tarif_tambahan_str[pilihan_fasilitas_tambahan]}")

# Tambah Peserta
def peserta_TAMBAH():

    os.system("cls")
    show_kode_paket_perjalanan()
    show_fasilitas_tambahan()

    # input nama peserta
    nama_peserta = input("\nNama Peserta\t\t:\t")
    while True:
        kode_paket = input("Kode Paket\t\t:\t")
        match kode_paket:
            case "01":

                # Harga Perjalanan & Rute Perjalanan
                tarif_perjalanan, rute_perjalanan = kolom_tarif_perjalanan_int[0], kolom_rute_perjalanan[0]
                tarif_perjalanan_str, min_peserta = kolom_tarif_perjalanan_str[0], kolom_min_peserta[0]
                break

            case "02":

                # Harga Perjalanan & Rute Perjalanan
                tarif_perjalanan, rute_perjalanan = kolom_tarif_perjalanan_int[1], kolom_rute_perjalanan[1]
                tarif_perjalanan_str, min_peserta = kolom_tarif_perjalanan_str[1], kolom_min_peserta[1]
                break

            case "03":

                # Harga Perjalanan & Rute Perjalanan
                tarif_perjalanan, rute_perjalanan = kolom_tarif_perjalanan_int[2], kolom_rute_perjalanan[2]
                tarif_perjalanan_str, min_peserta = kolom_tarif_perjalanan_str[ 2], kolom_min_peserta[2]
                break

            case "04":

                # Harga Perjalanan & Rute Perjalanan
                tarif_perjalanan, rute_perjalanan = kolom_tarif_perjalanan_int[3], kolom_rute_perjalanan[3]
                tarif_perjalanan_str, min_peserta = kolom_tarif_perjalanan_str[3], kolom_min_peserta[3]
                break

    print(f"Nama Paket\t\t:\t{rute_perjalanan} / {min_peserta}")
    print(f"Tarif Paket\t\t:\t{tarif_perjalanan_str}")

    # input kode tambahan
    while True:
        kode_tambahan = input("Kode Tambahan\t\t:\t")
        match kode_tambahan:
            case "A":

                # Harga Tambahan & Fasilitas
                tarif_tambahan_int, fasilitas, tarif_tambahan_str = kolom_tarif_tambahan_int[0], kolom_fasilitas[0], kolom_tarif_tambahan_str[0]
                break

            case "B":

                # Harga Tambahan & Fasilitas
                tarif_tambahan_int, fasilitas, tarif_tambahan_str = kolom_tarif_tambahan_int[1], kolom_fasilitas[1], kolom_tarif_tambahan_str[1]
                break

            case "C":

                # Harga Tambahan & Fasilitas
                tarif_tambahan_int, fasilitas, tarif_tambahan_str = kolom_tarif_tambahan_int[2], kolom_fasilitas[2], kolom_tarif_tambahan_str[2]
                break

    print(f"Fasilitas\t\t:\t{fasilitas}")
    print(f"Tarif Tambahan\t\t:\t{tarif_tambahan_str}")

    jumlah_tarif = tarif_perjalanan + tarif_tambahan_int
    print(f"Total Tarif\t\t:\tRp. {jumlah_tarif:,} ")

    # PPN 11%
    harga_ppn = (jumlah_tarif * 11) / 100
    print(f"PPN (11%)\t\t:\tRp. {harga_ppn:,} ")

    # Total Bayar
    jumlah_bayar = jumlah_tarif + harga_ppn
    print(f"Jumlah Biaya\t\t:\tRp. {jumlah_bayar:,} ")

    # Store Data
    data = f"{nama_peserta} {Fore.YELLOW}/{Fore.RESET} {rute_perjalanan} {Fore.YELLOW}/{Fore.RESET} {fasilitas} {Fore.YELLOW}/{Fore.RESET} Rp. {jumlah_bayar:,} {Fore.GREEN}]{Fore.RESET}"
    with open("DataTransaksi.txt", "a") as txt:
        txt.write(str(data) + "\n")   
    print(f"\n{Fore.GREEN}Data Berhasil Disimpan{Fore.RESET}")

    txt.close()
    interaksi()

# Lihat Peserta
def peserta_LIHAT():
    os.system("cls")
    print("}"f"{Fore.RED}------------------------------{Fore.RESET}{Fore.GREEN} LIHAT PESERTA {Fore.RESET}{Fore.RED}------------------------------{Fore.RESET}""{")

    # Memanggil Fungsi Show Peserta
    show_peserta()
    interaksi()

# Fungsi Menghapus Data Peserta
def peserta_HAPUS():

    os.system("cls")
    print("}"f"{Fore.RED}------------------------------{Fore.RESET}{Fore.GREEN} HAPUS PESERTA {Fore.RESET}{Fore.RED}------------------------------{Fore.RESET}""{")
    with open("DataTransaksi.txt", "r") as txt:
        data_transaksi = txt.readlines()
        jml_peserta = len(data_transaksi)
    show_peserta()

    #  Pilih Nomor Peserta
    hapus_nomor = int(input(f"\n{Fore.YELLOW}${Fore.RESET}No. Peserta >> "))
    if hapus_nomor - 1 not in range(jml_peserta):
        print(f"{Fore.RED}Peserta Tidak Ada{Fore.RESET}")
        interaksi()

    # menghapus data peserta
    with open("DataTransaksi.txt", "r") as txt:
        baris = txt.readlines()
        baris.pop(hapus_nomor - 1)

    # Menimpa Baris Kosong
    with open("DataTransaksi.txt", "w") as txt:
        txt.write("".join(baris))
    os.system("cls")
    show_peserta()
    print(f"\n{Fore.GREEN}Data Berhasil Dihapus{Fore.RESET}")
    txt.close()
    interaksi()

# Fungsi Cari Peserta

def peserta_CARI():
    os.system("cls")
    print("}"f"{Fore.RED}------------------------------{Fore.RESET}{Fore.GREEN} CARI PESERTA {Fore.RESET}{Fore.RED}------------------------------{Fore.RESET}""{")

    # Membuat Variabel Data Peserta
    with open("DataTransaksi.txt", "r") as txt:
        data_transaksi = txt.readlines()
    nama_peserta = input(f"\n{Fore.YELLOW}${Fore.RESET}Nama Peserta >> ")
    if nama_peserta == "":
        print(f"{Fore.RED}Nama Peserta Tidak Boleh Kosong{Fore.RESET}")
        interaksi()
    print("\n}"f"{Fore.RED}-----{Fore.RESET}{Fore.GREEN} HASIL PENCARIAN {Fore.RESET}{Fore.RED}-----{Fore.RESET}""{\n")
    for index in range(len(data_transaksi)):
        if nama_peserta + " " in data_transaksi[index]:
            print(
                f"{Fore.GREEN}[{Fore.RESET}  {Fore.YELLOW}{index+1}{Fore.RESET}  {Fore.GREEN}][{Fore.RESET} {data_transaksi[index]}")
    interaksi()

# Fungsi Menampilkan Data Peserta
def show_peserta():

    # Variabel Data Peserta
    with open("DataTransaksi.txt", "r") as txt:  
        data_transaksi = txt.readlines()     
        jml_peserta = len(data_transaksi)
    print(f"\n{Fore.GREEN}[{Fore.RESET} {Fore.YELLOW}No.{Fore.RESET} {Fore.GREEN}][{Fore.RESET} Nama Peserta {Fore.YELLOW}/{Fore.RESET} Paket {Fore.YELLOW}/{Fore.RESET} Tambahan {Fore.YELLOW}/{Fore.RESET} Total Bayar {Fore.GREEN}]{Fore.RESET}\n")

    # Perulangan for
    for index in range(jml_peserta):
        print(
            f"{Fore.GREEN}[{Fore.RESET}{Fore.YELLOW}  {index+1}{Fore.RESET}  {Fore.GREEN}][{Fore.RESET} {data_transaksi[index]}")
    return jml_peserta, data_transaksi


# Interaksi Akhir
def interaksi():

    input("\nTekan Enter Untuk Kembali..")
    os.system("cls")
    menu()

# Fungsi Menu
def menu():

    menu = 5

    # Perulangan While
    while True:
        try:
            print(f'''{Fore.YELLOW}
 ____    _____     __________
|  _  \ |  __  \  |___    ___|
| | )  |  |   \ \     |  |  _ __ __ _     _  ____  _   __ __ _  _ ___
|  __ /   |   | |     |  || '__/  _' |\  / /  _  \| |_/ /  _' || '__/
|  |    | |__/ /      |  || |  | (_| | \/ /   __ /   _ \  (_| || |
|__|    |_____/   o   |__||_|   \__'_|\__/ \_____||_| \_\___'_||_|
{Fore.RESET}''')

            print(
                "\t}"f"{Fore.RED}---------------------------------------------{Fore.RESET}""{")
            print("}"f"{Fore.RED}--------------------- {Fore.GREEN}Tiket Traveler{Fore.RESET} {Fore.RED}------------------------{Fore.RESET}""{")
            print(
                "\t}"f"{Fore.RED}---------------------------------------------{Fore.RESET}""{\n")
            print(
                f"\t{Fore.GREEN}[{Fore.RESET} 1 {Fore.GREEN}] {Fore.RESET}{Fore.YELLOW}Tambah Peserta{Fore.RESET}")
            print(
                f"\t{Fore.GREEN}[{Fore.RESET} 2 {Fore.GREEN}] {Fore.RESET}{Fore.YELLOW}Lihat Peserta{Fore.RESET}")
            print(
                f"\t{Fore.GREEN}[{Fore.RESET} 3 {Fore.GREEN}] {Fore.RESET}{Fore.YELLOW}Hapus Peserta{Fore.RESET}")
            print(
                f"\t{Fore.GREEN}[{Fore.RESET} 4 {Fore.GREEN}] {Fore.RESET}{Fore.YELLOW}Cari Peserta{Fore.RESET}")
            print(
                f"\t{Fore.GREEN}[{Fore.RESET} 5 {Fore.GREEN}] {Fore.RESET}{Fore.YELLOW}Exit{Fore.RESET}")

            # Pilihan Menu
            pilih = int(input(f"\n\t{Fore.YELLOW}${Fore.RESET}Pilih Menu >> "))
            if pilih > menu or pilih < 1:
                print(f"\n{Fore.RED}! Menu Tidak Ada !{Fore.RESET}")
                continue

            # Metode Dictionary
            selecting_menu = {
                1: peserta_TAMBAH,
                2: peserta_LIHAT,
                3: peserta_HAPUS,
                4: peserta_CARI,
                5: exit
            }

            # Metode get() untuk mengambil nilai dari dictionary
            return selecting_menu.get(int(pilih))()
        except ValueError:
            print(f"\n{Fore.RED}! Menu Tidak Ada !{Fore.RESET}")
            continue

if __name__ == '__main__':
    menu()
