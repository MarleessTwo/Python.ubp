# Soal No #10
# Menentukan Nilai Akhir dan Nilai Index Dari Nilai Hasil Tugas, UTS, dan UAS

def main():
    tugas = eval(input("Masukkan Nilai Tugas: "))
    uts = eval(input("Masukkan Nilai UTS: "))
    uas = eval(input("Masukkan Nilai UAS: "))

    akhir = int((tugas*20/100) + (uts*30/100) + (uas*50/100))

    if akhir >= 80:
        print("Nilai Akhir:", akhir)
        print("Nilai Index: A")
    elif akhir >= 68:
        print("Nilai Akhir:", akhir)
        print("Nilai Index: B")
    elif akhir >= 56:
        print("Nilai Akhir:", akhir)
        print("Nilai Index: C")
    elif akhir >= 45:
        print("Nilai Akhir:", akhir)
        print("Nilai Index: D")
    else:
        print("Nilai Akhir:", akhir)
        print("Nilai Index: E")


main()
