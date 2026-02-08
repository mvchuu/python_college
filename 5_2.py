from functools import wraps

class ResetKorutyny(Exception):
    pass

def korutyna(func):
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return primer

@korutyna
def srednia_kroczaca():
    suma = 0.0
    licznik = 0
    while True:
        try:
            nowa_liczba = yield
            suma += nowa_liczba
            licznik += 1
            print(f"Otrzymana nowa liczbe: {nowa_liczba}, Nowa srednia wynosi: {suma/licznik:.2f}")
        except ResetKorutyny:
            print("BLAD: korutyna zzresetowana.")
            suma = 0.0
            licznik = 0

kalkulator = srednia_kroczaca()

kalkulator.send(10)
kalkulator.send(20)

kalkulator.throw(ResetKorutyny)

kalkulator.send(5)
