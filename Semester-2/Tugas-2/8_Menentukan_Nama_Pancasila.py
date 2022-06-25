# Soal No #8
# Menentukan Nama Sila Dari Nomor Pancasila
inputUser = int(input("Masukan Nomor 1 - 5 Dalam Pancasila: "))


def switch(case):

    if case == 1:
        print("Ketuhanan Yang Maha Esa")

    elif case == 2:
        print("Kemanusiaan Yang Adil dan Beradab")

    elif case == 3:
        print("Persatuan Indonesia")

    elif case == 4:
        print("Kerakyatan Yang Dipimpin Oleh Hikmat Kebijksanaan Dalam Permusyawaratan / Perwakilan")

    elif case == 5:
        print("Keadilan Sosial Bagi Seluruh Rakyat Indonesia")

    else:
        print("Mohon Masukan Nomor 1-7")


# Memanggil Fungsi Switch
switch(inputUser)
