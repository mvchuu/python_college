class Gracz:
    liczba_graczy = 0

    def __init__(self, imie, hp):
        self.imie = imie
        self.hp = hp
        Gracz.liczba_graczy += 1

    def __str__(self):
        return f"Gracz {self.imie} (HP:{self.hp})" 

    def __repr__(self):
        return f"Gracz(imie={self.imie}, hp={self.hp})"

    def pokaz_status(self):
        print(f"Gracz: {self.imie}, HP: {self.hp}")

    def otrzymaj_obrazenia(self, ilosc):
        self.hp -= ilosc
        print(f"Gracz: {self.imie}, otrzymuje: {ilosc} obrazen")

print(Gracz.liczba_graczy)

gracz_1 = Gracz("Aragorn", 100)
gracz_2 = Gracz("Frodo", 50)

print(Gracz.liczba_graczy)

