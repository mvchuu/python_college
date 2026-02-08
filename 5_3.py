from functools import wraps

def korutyna(func):
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return primer

class ResetProcesora(Exception):
    pass

@korutyna
def procesor_polecen():
    dane = []
    print("\n---PROCESOR POLECEN GOTOWY---")
    dane = []
    while True:
        try:
            polecenie = yield
            czesci = polecenie.strip().split(":", 1)
            akcja = czesci[0].upper()
            wartosc = czesci[1] if len(czesci) > 1 else None

            if akcja == "DODAJ":
                dane.append(wartosc)
                print(f"Dodano: {wartosc}")
            elif akcja == "USUN":
                if wartosc in dane:
                    dane.remove(wartosc)
                    print(f"Usunieto: {wartosc}")
                else:
                    print(f"Nie mozna usunac: brak {wartosc}")
            elif akcja == "POKAZ":
                print(f"Aktualne dane: {dane}")
            else:
                print(f"BLAD: Nieznana akcja: {akcja}")
        except ResetProcesora:
            print("\n---RESETOWANIE PROCESORA---")
            dane = []
        except Exception as e:
            print("Wystapil nieoczekiwany blad: {e}")

procesor = procesor_polecen()

procesor.send("DODAJ:jablko")
procesor.send("DODAJ:banan")
procesor.send("DODAJ:arbuz")
procesor.send("POKAZ")
procesor.send("USUN:banan")
procesor.send("POKAZ")

procesor.throw(ResetProcesora)
procesor.send("POKAZ")
