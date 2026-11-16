# Tuple: tidak bisa diubah setelah dibuat
warna = ("merah", "hijau", "biru")

# Akses elemen
print(warna[1]) # hijau

# Tuple tidak bisa diubah
# warna[0] = "kuning" # Error

# Tapi bisa diakses dengan loop
for w in warna:
    print(w)
