# Soal No. #3
# Menghitung Luas dan Keliling Lingkaran Dari Nilai Jari Jari Lingkaran Yang DIinputkan

jari_jari = float(input("Masukkan jari-jari lingkaran: "))


def luas_lingkaran(jari_jari):
    luas_lingkaran = 3.14 * jari_jari ** 2
    return luas_lingkaran


def luas_keliling(jari_jari):
    luas_keliling = 2 * 3.14 * jari_jari
    return luas_keliling


def main():
    print("Luas Lingkaran: ", luas_lingkaran(jari_jari), "cm")
    print("Luas Keliling: ", format(luas_keliling(jari_jari), ".1f"), "cm")


if __name__ == "__main__":
    main()
