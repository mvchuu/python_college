import pickle

class StanGry:
    def __init__(self, nazwa_gracza:str, punkty:int, ekwipunek:list):
        self.nazwa_gracza = nazwa_gracza
        self.punkty = punkty
        self.ekwipunek = ekwipunek

    def __repr__(self):
        return f"Nazwa Gracza: {self.nazwa_gracza} (Punkty: {self.punkty}, Ekwipunek: {self.ekwipunek})"


save_1 = StanGry("Guts", 33, ["Miecz Berserkera"])

save = "stan_gry.pkl"

with open(save, "wb") as file:
    pickle.dump(save_1, file)

with open(save, "rb") as file:
    wczytany_stan = pickle.load(file)
    print(type(wczytany_stan))
    print(wczytany_stan)
