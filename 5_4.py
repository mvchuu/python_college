class Odliczanie:
    def __init__(self, start:int):
        self.start = start

    def __iter__(self):
        print("Rozpoczynam odliczanie:")
        liczba = self.start
        while liczba > 0:
            yield liczba
            liczba -= 1
        yield "!START!"

odliczanie_do_startu = Odliczanie(5)

for krok in odliczanie_do_startu:
    print(krok)
