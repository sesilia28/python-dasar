# Abstraction pada sistem pembayaran
from abc import ABC, abstractmethod

class Pembayaran(ABC):
    @abstractmethod
    def bayar(self, jumlah):
        pass

class Gopay(Pembayaran):
    def bayar(self, jumlah):
        print(f"Bayar {jumlah} menggunakan GoPay")

class Dana(Pembayaran):
    def bayar(self, jumlah):
        print(f"Bayar {jumlah} menggunakan Dana")

# Menggunakan abstraction
def proses_pembayaran(pembayaran, jumlah):
    pembayaran.bayar(jumlah)

proses_pembayaran(Gopay(), 35000)
proses_pembayaran(Dana(), 60000)
