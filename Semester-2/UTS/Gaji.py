# UTS
# Menghitung Gajih Pegawai
import os

# Looping Input
while True:
    os.system('cls')
    try:
        print('''
[ Golongan  | Gaji Pokok |    Tunjangan    | Lembur/jam ]
[=======================================================]
[    A      |   500.000  | 10% Gaji Pokok | Rp. 5.000   ]
[    B      |   700.000  | 15% Gaji Pokok | Rp. 7.500   ]
[    C      |   900.000  | 20% Gaji Pokok | Rp. 10.000  ]
[=======================================================]
''')
        input_nama = input("Nama : ")
        print("Golongan (A/B/C)")
        input_gol = input()
        if input_gol == 'A' or input_gol == 'B' or input_gol == 'C' or input_gol == 'a' or input_gol == 'b' or input_gol == 'c':
            break
        else:
            print("Golongan Tidak Dikenali")
        continue
    except:
        print("Golongan Tidak Dikenali")

while True:
    try:
        input_jamker = int(input("Total Jam Kerja : "))
        break
    except ValueError:
        print("Inputan Tidak Dikenali")
        continue


# Fungsi Golongan
def Golongan(input_gol):
    Lembur = 0

    if input_gol == 'A' or input_gol == 'a':
        Gaji = 500000
        Tunjangan = (Gaji * 10) / 100

        if input_jamker > 200:
            Lembur = (input_jamker - 200) * 5000
            Total = Gaji + Tunjangan + Lembur
            return Gaji, Tunjangan, Lembur, Total

        elif input_jamker <= 200:
            Total = Gaji + Tunjangan
            return Gaji, Tunjangan, Lembur, Total

    elif input_gol == 'B' or input_gol == 'b':
        Gaji = 700000
        Tunjangan = (Gaji * 15) / 100

        if input_jamker > 200:
            Lembur = (input_jamker - 200) * 7500
            Total = Gaji + Tunjangan + Lembur
            return Gaji, Tunjangan, Lembur, Total

        elif input_jamker <= 200:
            Total = Gaji + Tunjangan
            return Gaji, Tunjangan, Lembur, Total

    elif input_gol == 'C' or input_gol == 'c':
        Gaji = 900000
        Tunjangan = (Gaji * 20) / 100

        if input_jamker > 200:
            Lembur = (input_jamker - 200) * 10000
            Total = Gaji + Tunjangan + Lembur
            return Gaji, Tunjangan, Lembur, Total

        elif input_jamker <= 200:
            Total = Gaji + Tunjangan
            return Gaji, Tunjangan, Lembur, Total


# Output
print("=" * 50)
print("               DATA PEGAWAI")
print("=" * 50)
print("\n")
print("Nama                 : ", input_nama)
print("Golongan             : ", input_gol)
print("Total Jam Kerja      : ", input_jamker, "jam")
print("=" * 50)
print("               PENGHITUNGAN GAJI")
print("=" * 50)
print("Gaji Pokok           : Rp.", format(Golongan(input_gol)[0], ",.0f"))
print("Tunjangan            : Rp.", format(Golongan(input_gol)[1], ",.0f"))
print("Lembur               : Rp.", format(Golongan(input_gol)[2], ",.0f"))
print("Total Gaji           : Rp.", format(Golongan(input_gol)[3], ",.0f"))
