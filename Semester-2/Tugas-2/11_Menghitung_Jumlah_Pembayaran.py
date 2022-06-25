# Soal No #11
# Menghitung Jumlah Pembayaran Dari 2 Pilihan Yang Dimana Akan Mendapatkan Potongan

import os

while True:
    os.system('cls')
    try:
        print('''
[ Paket | Menu Hidangan |    Harga   ]
[====================================]
[   A   |  Ayam Penyet  | Rp. 15.000 ]
[   B   |  Pecel Lele   | Rp. 12.000 ]
[   C   |  Nasi Goreng  | Rp. 10.000 ]
[   D   |  Jus Buah     | Rp. 8.000  ]
[   E   |  Teh Manis    | Rp. 2.000  ]
        ''')
        print("Mau Paket Makana Yang Mana Nih? (A/B/C)")
        Pilih1 = input("Pilih : ")
        if Pilih1 == "A" or Pilih1 == "a" or Pilih1 == "B" or Pilih1 == "b" or Pilih1 == "C" or Pilih1 == "c":
            break
        else:
            print("\n! Hanya Ada A Sampai C !")
            continue
    except:
        print("\n! Hanya Ada A Sampai C !")
        continue


while True:
    try:
        print("\nMinumnya? (D/E)")
        Pilih2 = input("Pilih : ")
        if Pilih2 == "D" or Pilih2 == "d" or Pilih2 == "E" or Pilih2 == "e":
            break
        else:
            print("\n! Hanya Ada D dan E !")
            continue
    except:
        print("\n! Hanya Ada D dan E !")
        continue


def harga_makanan(Pilih1):
    harga_makanan = {
        "A": 15000,
        "B": 12000,
        "C": 10000,
        #
        "a": 15000,
        "b": 12000,
        "c": 10000
    }
    return harga_makanan.get(Pilih1)


def harga_minuman(Pilih2):
    harga_minuman = {
        "D": 8000,
        "E": 2000,
        #
        "d": 8000,
        "e": 2000
    }
    return harga_minuman.get(Pilih2)


Total_Harga = harga_makanan(Pilih1) + harga_minuman(Pilih2)

if Total_Harga > 20000:
    Potongan = Total_Harga - 2000
    print("\n! Kamu Dapat Potongan Harga Sebesar Rp. 2.000 !")
    print(f"Harga    : Rp.", format(Total_Harga, ","))
    print(f"Potongan : Rp. 2.000")
    print(f"Total    : Rp.", format(Potongan, ","))
else:
    print("\n! Total Harga : Rp.", format(Total_Harga, ","))
