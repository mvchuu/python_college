class Gracz:
    def __init__(self, imie, hp):
        self.imie = imie
        self.hp = hp

    def __str__(self):
        return f"Gracz {self.imie} (HP:{self.hp})" 

    def __repr__(self):
        return f"Gracz(imie={self.imie}, hp={self.hp})"

    def pokaz_status(self):
        print(f"Gracz: {self.imie}, HP: {self.hp}")

    def otrzymaj_obrazenia(self, ilosc):
        self.hp -= ilosc
        print(f"Gracz: {self.imie}, otrzymuje: {ilosc} obrazen")

gracz_obj = Gracz("Aragorn", 100)
gracz_obj.pokaz_status()
gracz_obj.otrzymaj_obrazenia(15)
gracz_obj.pokaz_status()

print(gracz_obj)
print(repr(gracz_obj))
