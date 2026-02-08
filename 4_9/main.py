import json

def wczytaj_konfiguracje(sciezka:str) -> dict:
    try:
        with open(sciezka, "r", encoding = "utf-8") as file:
            dane = json.load(file)
            return dane

    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

dane = wczytaj_konfiguracje("konfiguracja.json")
print(dane['baza_danych']['uzytkownik'])
