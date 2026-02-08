slowo = (input("Podaj dowolne slowo: ")).lower()

licznik_samoglosek = 0

samogloski = ["a", "e", "i", "o", "u", "y"]

for litera in slowo:
    if litera in samogloski:
        licznik_samoglosek += 1

print(f"Slowo {slowo} ma {licznik_samoglosek} samoglosek.")
