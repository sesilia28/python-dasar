# Menambah data di akhir file tanpa menghapus isi lama
file = open("data.txt", "a")
file.write("Baris tambahan...\n")
file.close()
