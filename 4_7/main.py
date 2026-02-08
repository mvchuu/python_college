import csv

def wczytaj_pracownikow(sciezka_pliku:str) -> list:
    pracownicy = []

    try:
        with open(sciezka_pliku, "r") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                try:
                    pensja = int(row['pensja'])

                    pracownicy.append({
                        'imie':row['imie'],
                        'stanowisko':row['stanowisko'],
                        'pensja':pensja
                    })
                except ValueError:
                    return f"Blad kowenrsji: '{row['pensja']}' nie jest liczba dla {row['imie']}."
    except FileNotFoundError:
        return f"Plik {sciezka_pliku} nie zostal znaleziony."
    
    return pracownicy

plik = "pracownicy.csv"

pracownicy = wczytaj_pracownikow(plik)
print(pracownicy)
