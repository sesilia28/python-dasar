# else dijalankan jika tidak ada error, finally selalu dijalankan
try:
    angka = 18 / 3
except ZeroDivisionError:
    print("Error: Tidak bisa bagi nol!")
else:
    print("Perhitungan berhasil, hasil:", angka)
finally:
    print("Selesai memproses.")
