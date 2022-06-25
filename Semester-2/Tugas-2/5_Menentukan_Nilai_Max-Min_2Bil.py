# Soal No #5
# Menentukan Nilai Minimum dan Maksimum dari 2 Bilangan
print("\n~~ Menentukan Nilai Minimum dan Maksimum dari 2 Bilangan ~~~\n")

n1 = int(input("Masukkan Nilai Pertama: "))
n2 = int(input("Masukkan Nilai Kedua: "))

# Memeriksa Nilai Minimum dan Maksimum
if n1 < n2:
    print(f"{n1} Adalah Nilai >..Minimum..<")
    print(f"{n2} Adalah Nilai <..Maksimum..>")

elif n1 > n2:
    print(f"{n2} Adalah Nilai >..Minimum..<")
    print(f"{n1} Adalah Nilai <..Maksimum..>")

else:
    print(f"{n1} Adalah Nilai >..Minimum..<")
    print(f"{n2} Adalah Nilai <..Maksimum..>")
