# Polymorphism dengan fungsi
class Kucing:
    def suara(self):
        return "Meow"

class Anjing:
    def suara(self):
        return "Guk guk"

def cetak_suara(hewan):
    print(hewan.suara())

cetak_suara(Kucing())
cetak_suara(Anjing())

# Fungsi bawaan len() juga polymorphism
print(len("Sesilia")) # string
print(len([10, 20, 30, 40])) # list
print(len({"a": 1, "b": 2})) # dictionary
