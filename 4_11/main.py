from pydantic import BaseModel, ValidationError


class SpecyfikacjaModel:
    def __init__(self, procesor:str, ram_gb:int):
        self.procesor = procesor
        self.ram_gb = ram_gb



class ProduktModel:
    def __init__(self, cena:float, dostepny:bool, tagi:list[str], specyfikacja:SpecyfikacjaModel):
        self.cena = cena
        self.dostepny = dostepny
        self.tagi = tagi
        self.specyfikacja = specyfikacja

    def wczytaj_i_waliduj_produkt(self, sciezka:str) -> ProduktModel | None:
        try:
            with open(sciezka, "r", encoding="utf-8") as file:
                produkt = ProduktModel.parse_obj(sciezka)
        except FileNotFoundError:
            print("BLAD: Nie znaleziono pliku!")
        except json.JSONDecodeError:
            print("BLAD: Nieprawidlowa skladnia pliku!")
        except pydantic.ValidationError:
            print("BLAD: Nieprawidlowe wartosci!")
            return None
        return produkt

produkt_1 = wczytaj_i_waliduj_produkt("konfiguracja.json")
print(produkt_1.nazwa_produktu)
print(produkt_1.specyfikacja.procesor)
