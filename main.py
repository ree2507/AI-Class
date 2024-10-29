# Daftar data yang akan dicari
a = [2, 2, 1, 3, 5, 5, 5, 7, 2, 10]

# Variabel yang ingin dicari
x = 2

# Mencari jumlah kemunculan dan indeks dari x dalam list a
jumlah_x = a.count(x)
indeks_x = [index for index, value in enumerate(a) if value == x]

# Menampilkan hasil
print(f"Variabel x = {jumlah_x} index {', '.join(map(str, indeks_x))}")
