# Soal No #4
# Membuat Sistem Login dan Validasi Akun

import os


# Fungsi Menu
def menu():
    while True:
        try:
            print("Pilih Menu: ")
            print("1. Buat Akun Baru")
            print("2. Login")
            print("3. Keluar")
            pilih = input("Masukkan Pilihan Anda: ")

            selecting = {
                1: buat_akun,
                2: login,
                3: exit
            }

            return selecting.get(int(pilih))()
        except ValueError:
            print("\n! Inputan Harus Berupa Angka ! \n")
            continue


# Fungsi Membuat Akun
def buat_akun():
    os.system("cls")

    username = input("Buat Username : ")
    password = input("Buat Password : ")

    data = {
        "username": username,
        "password": password
    }

    with open("Semester-2/Tugas-2/.4_SistemLogin/Login.txt", "a") as file:
        file.write(str(data) + "\n")

    print("Akun Berhasil Dibuat")
    input("Tekan Enter Untuk Kembali..")
    os.system("cls")
    return menu()


# Fungsi login akun
def login():
    os.system("cls")

    username_login = input("Username : ")
    password_login = input("Password : ")

    # Validasi Login
    with open("Semester-2/Tugas-2/.4_SistemLogin/Login.txt", "r") as file:
        for line in file:
            data = eval(line)
            if data["username"] == username_login and data["password"] == password_login:
                print("Login Berhasil")
                print("Selamat Datang", data["username"])
                input("Tekan Enter Untuk Kembali..")
                os.system("cls")
                return menu()
            else:
                print("Login Gagal")
                input("Tekan Enter Untuk Kembali..")
                os.system("cls")
                return menu()


# memanggil fungsi buat akun
if __name__ == '__main__':
    menu()
