# *args dan **kwargs
def jumlahkan(*angka):
    total = sum(angka)
    print("Total:", total)

jumlahkan(2, 4, 6, 8, 10) # Bisa input banyak angka

def biodata(**data):
    for key, value in data.items():
        print(f"{key}: {value}")

biodata(nama="Sesilia", sekolah="SMKN 2 Subang", kota="Subang")
