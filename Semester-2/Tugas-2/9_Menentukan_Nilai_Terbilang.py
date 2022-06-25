# Soal No #9
# Menentukan Nilai terbilang dari angka yang diinputkan

bilangan = int(input("Masukkan bilangan: "))

# Menentukan bilangan terbilang
if bilangan < 10:
    print(
        f"Angka {bilangan} Adalah Bilangan Satuan")
elif bilangan < 100:
    print(
        f"Angka {bilangan} Adalah Bilangan Puluh")
elif bilangan < 1000:
    print(
        f"Angka {bilangan} Adalah Bilangan Ratus")
elif bilangan < 1000000:
    print(
        f"Angka {bilangan} Adalah Bilangan Ribu")
else:
    print("Angka Terlalu Besar")
