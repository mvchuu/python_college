class Gracz:
    def __init__(self, imie, hp):
        self.imie = imie
        self.hp = hp

gracz_obj = Gracz("Aragorn", 100)
print(gracz_obj.imie)
print(gracz_obj.hp)
