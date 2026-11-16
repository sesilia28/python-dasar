# Polymorphism pada method: nama sama, perilaku berbeda
class Kucing:
    def suara(self):
        return "Meow"

class Anjing:
    def suara(self):
        return "Guk guk"

hewan = [Kucing(), Anjing()]
for h in hewan:
    print(h.suara())
