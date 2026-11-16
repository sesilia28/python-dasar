# Menggunakan with agar file otomatis tertutup
with open("data.txt", "r") as file:
    isi = file.read()
    print(isi)
