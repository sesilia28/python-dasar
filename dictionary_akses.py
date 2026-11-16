# Mengakses data dictionary
siswa = {"nama": "Sesilia", "jumlah_buku": 12, "kota": "Subang"}

print(siswa["nama"]) # Sesilia
print(siswa.get("jumlah_buku")) # 12
print(siswa.get("hobi")) # None, tidak error karena memakai get()
