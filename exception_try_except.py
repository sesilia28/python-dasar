# Tanpa exception handling, program langsung berhenti:
# hasil = 24 / 0 # ZeroDivisionError: division by zero

# Menangani error dengan try-except
try:
    angka = 24
    hasil = angka / 0
    print("Hasil:", hasil)
except ZeroDivisionError:
    print("Error: Tidak bisa membagi dengan nol!")
