f = open("wiek.txt", "w")
f.write("25")
f.close()

def oblicz_rok_urodzenia(sciezka_pliku):
    aktualny_rok = 2026
    try:
        f = open(sciezka_pliku, "r")
        wiek = int(f.read())
        rok_urodzenia = aktualny_rok - wiek
        print(f"Rok urodzenia to: {rok_urodzenia}")
    except FileNotFoundError:
        return "BLAD: nie znaleziono pliku!"
    except ValueError:
        return "BLAD: zawartosc pliku nie jest poprawna liczba"
    finally:
        f.close()
oblicz_rok_urodzenia("wiek.txt")
