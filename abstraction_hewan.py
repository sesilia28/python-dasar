# Abstract class dengan modul abc
from abc import ABC, abstractmethod

class Hewan(ABC):
    @abstractmethod
    def suara(self):
        pass

# Subclass yang mengimplementasikan abstract method
class Kucing(Hewan):
    def suara(self):
        return "Meow"

class Anjing(Hewan):
    def suara(self):
        return "Guk guk"

k = Kucing()
a = Anjing()
print(k.suara())
print(a.suara())

# Tidak bisa langsung membuat object dari class abstract
try:
    h = Hewan()
except TypeError:
    print("Class abstract tidak bisa dibuat objek langsung")
