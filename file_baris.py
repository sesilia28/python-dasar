# Membaca file baris per baris
file = open("data.txt", "r")
for baris in file:
    print(baris.strip()) # strip() untuk hapus newline
file.close()
