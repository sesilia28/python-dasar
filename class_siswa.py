# Membuat class
class Siswa:
    def __init__(self, nama, sekolah):
        self.nama = nama
        self.sekolah = sekolah

    def sapa(self):
        print(f"Halo, nama saya {self.nama} dari {self.sekolah}")

# Membuat object dari class
siswa1 = Siswa("Sesilia", "SMKN 2 Subang")
siswa2 = Siswa("Rani", "SMKN 2 Subang")

# Memanggil method
siswa1.sapa()
siswa2.sapa()
