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

class Mag(Gracz):
    def __init__(self, imie, hp, mana):
        super().__init__(imie, hp)
        self.mana = mana

    def przedstaw_sie(self):
        print(f"Nazywam sie: {self.imie}, posiadam: {self.mana} many")

class Niziolek(Gracz):
    def __init__(self, imie, hp):
        super().__init__(imie, hp)

gracz_1 = Wojownik("Aragorn", 100, 30)
gracz_2 = Mag("Gandalf", 80, 60)
gracz_3 = Niziolek("Frodo", 50)

druzyna = [
    gracz_1, gracz_2, gracz_3
]

for gracz in druzyna:
    if isinstance(gracz, Mag):
        gracz.przedstaw_sie()
