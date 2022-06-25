import random
import datetime as dt

Line = ("="*75)

# Referensi Generator
huruf = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
angka = '1234567890'

data_string = huruf + angka

panjang_string = 16

random_ref = "".join(random.sample(data_string, panjang_string))

# Input Harga Item
Nm_item = input("Nama item \t: ")
Jml_item = int(input("Jumlah \t\t: "))
Hrg_item = int(input(f"Harga \t\t: Rp. "))

Nm_item2 = input("Nama item \t: ")
Jml_item2 = int(input("Jumlah \t\t: "))
Hrg_item2 = int(input(f"Harga \t\t: Rp. "))

Nm_item3 = input("Nama item \t: ")
Jml_item3 = int(input("Jumlah \t\t: "))
Hrg_item3 = int(input(f"Harga \t\t: Rp. "))

jumlah_uang = int(input("Jumlah uang \t: Rp. "))

# Struk Belanja
print(Line)

print(f"\n\t\t~~~ Toko Marleess Jaya ~~~ \n")

hari_ini = dt.datetime.now()
lokasi = f'''Marleess Jaya, jl. Raya Tamelang 16, 
                          Mekarjaya, Kec.Purwasari, Kabupaten Karawang,
                          Jawa Barat 41373'''
admin = 'Kasir Bangsat'

print(f'''
Tanggal \t\t: {hari_ini.strftime("%d/%m/%Y")}
Waktu \t\t\t: {hari_ini.strftime("%H:%M:%S")}
Lokasi \t\t\t: {lokasi}
Kode Referensi \t\t: {random_ref}
Admin \t\t\t: {admin}
''')

print(Line)
print(f'''\t\t\t\tBelanja
{Line}

~{Nm_item}
Jumlah : {Jml_item}
Rp. {Hrg_item:,}

~{Nm_item2}
Jumlah : {Jml_item2}
Rp. {Hrg_item2:,}

~{Nm_item3}
Jumlah : {Jml_item3}
Rp. {Hrg_item3:,}

{Line}
''')

# Transaksi dan Kembalian
total_item = Jml_item + Jml_item2 + Jml_item3
total_harga = (Hrg_item * Jml_item) + (Hrg_item2 * Jml_item2) + (Hrg_item3 * Jml_item3)

# PPN
PPN = 10
hitung_ppn = PPN * total_harga / 100

print(f'''
Tunai \t\t\t: Rp. {jumlah_uang:,}
Total item \t\t: {total_item}
Total harga \t\t: Rp. {total_harga:,}
PPN \t\t\t: Rp. {hitung_ppn:,}

kembalian \t\t: Rp. {jumlah_uang - total_harga - hitung_ppn:,}
''')
