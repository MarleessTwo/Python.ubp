# Soal No #6
# Menentukan Nilai Minimum dan Maksimum dari 3 Bilangan
print("\n~~ Menentukan Nilai Minimum dan Maksimum dari 3 Bilangan ~~~\n")

n1 = int(input("Masukkan Nilai Pertama: "))
n2 = int(input("Masukkan Nilai Kedua: "))
n3 = int(input("Masukkan Nilai Ketiga: "))

# Memeriksa Nilai Minimum dan Maksimum
if n1 <= n2 and n1 <= n3:
    min = n1
    if n2 <= n3:
        max = n3
        print("Nilai Minimum:", min)
        print("Nilai Maksimum:", max)
    else:
        max = n2
        print("Nilai Minimum:", min)
        print("Nilai Maksimum:", max)
elif n2 <= n1 and n2 <= n3:
    min = n2
    if n1 <= n3:
        max = n3
        print("Nilai Minimum:", min)
        print("Nilai Maksimum:", max)
    else:
        max = n1
        print("Nilai Minimum:", min)
        print("Nilai Maksimum:", max)
else:
    min = n3
    if n1 <= n2:
        max = n2
        print("Nilai Minimum:", min)
        print("Nilai Maksimum:", max)
    else:
        max = n1
        print("Nilai Minimum:", min)
        print("Nilai Maksimum:", max)
