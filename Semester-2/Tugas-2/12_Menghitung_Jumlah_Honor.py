# Soal No #12
# Menghitung Jumlah Honor Pegawai
import os

# Looping Input
while True:
    os.system('cls')
    try:
        print('''
[ Golongan  | Masa_Kerja |    Honor    ]    [ Grade | Transport ]
[======================================]    [===================]
[    A      |    <= 2    | Rp. 500.000 ]    [   1  | Rp. 10.000 ]
[           |     > 2    | Rp. 600.000 ]    [   2  | Rp. 12.000 ]
[======================================]    [   3  | Rp. 15.000 ]
[    B      |    <= 2    | Rp. 600.000 ]    [===================]
[           |     > 2    | Rp. 700.000 ]
[======================================]
[    C      |    <= 2    | Rp. 750.000 ]
[           |     > 2    | Rp. 850.000 ]
[======================================]
''')
        Nama = input("Nama : ")
        print("Golongan (A/B/C)")
        Gol = input()
        if Gol == 'A' or Gol == 'B' or Gol == 'C' or Gol == 'a' or Gol == 'b' or Gol == 'c':
            break
        else:
            print("Golongan Tidak Dikenali")
        continue
    except:
        print("Golongan Tidak Dikenali")

while True:
    try:
        print("Masa Kerja ")
        Masa_Kerja = int(input())
        print("Grade (1/2/3)")
        Grade = int(input())
        print("Jumlah Hari Kerja")
        Hari_Kerja = int(input())
        break
    except ValueError:
        print("Inputan Tidak Dikenali")
        continue


# Fungsi Golongan
def Golongan(Gol):
    if Gol == 'A' or Gol == 'a':
        if Masa_Kerja <= 2:
            Honor = (500000)
            return Honor
        elif Masa_Kerja > 2:
            Honor = (600000)
            return Honor
        return Gol
    elif Gol == 'B' or Gol == 'b':
        Gol = 'B'
        if Masa_Kerja <= 2:
            Honor = (600000)
            return Honor
        elif Masa_Kerja > 2:
            Honor = (700000)
            return Honor
        return Gol
    elif Gol == 'C' or Gol == 'c':
        Gol = 'C'
        if Masa_Kerja <= 2:
            Honor = (750000)
            return Honor
        elif Masa_Kerja > 2:
            Honor = (850000)
            return Honor
        return Gol
    else:
        return 0


# Fungsi Transport
def GT(Grade):
    if Grade == 1:
        Transport = (10000)
        return Transport
    elif Grade == 2:
        Transport = (12000)
        return Transport
    elif Grade == 3:
        Transport = (15000)
        return Transport
    else:
        return 0


# Penentuan Honor
Jumlah_Honor = Golongan(Gol) + (GT(Grade) * Hari_Kerja)
Jumlah_Transport = GT(Grade)

# Output
print("\n")
print("Nama                 : ", Nama)
print("Golongan             : ", Gol)
print("Masa Kerja           : ", Masa_Kerja, "Tahun")
print("Grade                : ", Grade)
print("Jumlah Hari Kerja    : ", Hari_Kerja, "Hari")
print("=" * 50)
print("Honor                : Rp.", format(Jumlah_Honor, ",.0f"))
print("Transport            : Rp.", format(Jumlah_Transport, ",.0f"))
