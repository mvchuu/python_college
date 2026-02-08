class Ekwipunek:
    def __init__(self):
        self.przedmioty = []

    def __iter__(self):
        return IteratorEkwipunku(self.przedmioty)

    def dodaj_przedmiot(self, przedmiot):
        self.przedmioty.append(przedmiot)

    def pokaz_przedmioty(self):
        print(f"Ekwipunek:")
        for przedmiot in self.przedmioty:
            print(przedmiot)

class IteratorEkwipunku:
    def __init__(self, lista_przedmiotow):
        self.lista_przedmiotow = lista_przedmiotow
        self.licznik_pozycji = 0

    def __next__(self):
        if self.licznik_pozycji < len(self.lista_przedmiotow):
            przedmiot = self.lista_przedmiotow[self.licznik_pozycji]
            self.licznik_pozycji += 1
            return przedmiot
        else:
            raise StopIteration

    def __iter__(self):
        return self


class Gracz:
    liczba_graczy = 0

    def __init__(self, imie, hp):
        self.imie = imie
        self._hp = 0
        self.hp = hp
        Gracz.liczba_graczy += 1
        self.ekwipunek = Ekwipunek()

    def __str__(self):
        return f"Gracz {self.imie} (HP:{self.hp})" 

    def __repr__(self):
        return f"Gracz(imie={self.imie}, hp={self.hp})"

    @staticmethod
    def sprawdz_poprawnosc_imienia(imie):
        if imie is not None and imie.istitle():
            True
        else:
            False
    
    def __eq__(self, other):
        if isinstance(other, Gracz) and self.imie == other.imie:
            return True
        else:
            return False

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, nowa_wartosc):
        if nowa_wartosc < 0:
            self._hp = 0
        else:
            self._hp = nowa_wartosc

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

    def __add__(self, other):
        return self.imie + " i " + other.imie
        return self.hp + other.hp
        return self.sila + other.sila

    @classmethod 
    def stworz_berserkera(cls, imie):
        hp = 80
        sila = 40
        return cls(imie, hp, sila)

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



eq = Ekwipunek()
eq.dodaj_przedmiot("Miecz")
eq.dodaj_przedmiot("Maczuga")
eq.dodaj_przedmiot("Noz")

for przedmiot in eq:
    print(przedmiot)
