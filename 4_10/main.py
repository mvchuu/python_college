import json

moje_dane = [
    {"ulubiony":"zolty", "nielubiany":"czarny"},
    {"ulubiony":"niebieski", "nielubiany":"zielony"}
]

def zapisz_jako_json(sciezka:str, dane:dict | list):
    try:
        with open(sciezka, "w", encoding="utf-8") as file:
            json.dump(dane, file, indent=4, ensure_ascii=False)
            print("Misja zakonczona sukcesem.")
    except IOError:
        print("BLAD: Problem wejsc/wyjsc.")

zapisz_jako_json("dane.json", moje_dane)
