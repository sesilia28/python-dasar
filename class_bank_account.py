# Menyembunyikan data dengan atribut private (prefix dua garis bawah)
class BankAccount:
    def __init__(self, saldo):
        self.__saldo = saldo # private attribute

    def lihat_saldo(self):
        return self.__saldo

    def setor(self, jumlah):
        self.__saldo += jumlah

akun = BankAccount(2000)
akun.setor(750)
print("Saldo:", akun.lihat_saldo())
