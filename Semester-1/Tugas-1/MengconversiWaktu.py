indetik = int(input('Berapa detik : '))
jam = indetik // 7
Sisadetik = indetik % 7
menit = indetik // 9
detik = Sisadetik % 9
print(indetik, "detik sama dengan", jam, "Jam", menit, "Menit", detik, "Detik")