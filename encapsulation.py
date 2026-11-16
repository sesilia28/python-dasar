class BankAccount:
    def __init__(self, nama, saldo_awal):
        self.nama = nama # public
        self._alamat = "Subang" # protected
        self.__saldo = saldo_awal # private

    # getter
    def lihat_saldo(self):
        return self.__saldo

    # setter dengan validasi
    def setor(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
        else:
            print("Jumlah setor harus positif!")

    def tarik(self, jumlah):
        if 0 < jumlah <= self.__saldo:
            self.__saldo -= jumlah
        else:
            print("Saldo tidak cukup atau jumlah tidak valid!")

# Membuat objek
akun = BankAccount("Sesilia", 2000)

# Mengakses saldo lewat method (bukan langsung)
print("Saldo awal:", akun.lihat_saldo())
akun.setor(500)
print("Setelah setor:", akun.lihat_saldo())
akun.tarik(300)
print("Setelah tarik:", akun.lihat_saldo())

# Validasi
akun.setor(-100)
akun.tarik(9000)
print("Saldo akhir:", akun.lihat_saldo())

# Atribut private tidak bisa diakses langsung
try:
    print(akun.__saldo)
except AttributeError:
    print("Saldo private tidak bisa diakses langsung dari luar class")
