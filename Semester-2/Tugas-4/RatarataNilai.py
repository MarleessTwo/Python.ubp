# Soal No. #1
# Menghitung Jumlah dan Rata-rata dari 5 Nilai Mata Kuliah

PDT, SD, EFC, MD, JDB = 80, 84, 70, 60, 100


def average(PDTeo, SD, EFC, MD, JDB):
    avr = (PDTeo + SD + EFC + MD + JDB) / 5
    return avr


def main():
    print("Rata-rata Nilai Mata Kuliah : ",
          average(PDT, SD, EFC, MD, JDB))


if __name__ == "__main__":
    main()
