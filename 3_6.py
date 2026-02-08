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

class Wojownik(Gracz):
    def __init__(self, imie, hp, sila):
        super().__init__(imie, hp)
        self.sila = sila
    
    def __str__(self):
        return f"Wojownik {self.imie} (HP:{self.hp}, SILA:{self.sila})"

    def atak(self):
     print(f"Wojownik {self.imie}, atakuje uzywajac {self.sila} sily")


gracz_1 = Wojownik("Aragorn", 100, 30)
print(gracz_1)
gracz_1.atak()
