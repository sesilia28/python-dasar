# Menggunakan super() untuk mengakses parent class
class Siswa:
    def __init__(self, nama, sekolah):
        self.nama = nama
        self.sekolah = sekolah

    def info(self):
        print(f"Nama: {self.nama}, Sekolah: {self.sekolah}")

class SiswaBaru(Siswa):
    def __init__(self, nama, sekolah, tahun_masuk):
        super().__init__(nama, sekolah) # memanggil constructor parent
        self.tahun_masuk = tahun_masuk

    def info(self):
        super().info() # memanggil method parent
        print(f"Tahun Masuk: {self.tahun_masuk}")

baru = SiswaBaru("Sesilia", "SMKN 2 Subang", 2025)
baru.info()
