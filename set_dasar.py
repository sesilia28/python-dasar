# Set: unik dan tidak berurutan
angka = {1, 2, 3, 3, 4, 5}
print(angka) # duplikat otomatis hilang

# Menambah dan menghapus elemen
angka.add(6)
angka.remove(2)
print(angka)

# Operasi himpunan
ganjil = {1, 3, 5, 7}
genap = {2, 4, 6, 8}
print(ganjil | genap) # Union
print(ganjil & genap) # Intersection
print(ganjil - genap) # Difference
