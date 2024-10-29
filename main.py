# Nama: Reyhan Dany_F55123095
# Kelas: TI C

a = [2, 2, 1, 3, 5, 5, 5, 7, 2, 10]

# Variabel yang ingin dicari, jika x = 2, maka index akan muncul sebanyak 3 kali pada index 0, 1, dan 8 pada list
x = 2

# Mencari jumlah kemunculan dan indeks dari x dalam list a
jumlah_x = a.count(x)
indeks_x = [index for index, value in enumerate(a) if value == x]

print(f"Variabel x = {jumlah_x} index {', '.join(map(str, indeks_x))}")
