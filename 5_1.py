from functools import wraps

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
        nowa_liczba = yield
        if nowa_liczba:
            suma += nowa_liczba
            licznik += 1
            print(f"Otrzymana nowa liczbe: {nowa_liczba}, Nowa srednia wynosi: {suma/licznik:.2f}")


kalkulator = srednia_kroczaca()

kalkulator.send(10)
kalkulator.send(20)
kalkulator.send(5)

