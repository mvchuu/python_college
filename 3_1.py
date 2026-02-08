pracownicy = [
    {"imie":"Anna", "stanowisko":"Specjalista", "pensja":4500},
    {"imie":"Piotr", "stanowisko":"Manager", "pensja":8000},
    {"imie":"Zofia", "stanowisko":"Specjalista", "pensja":5000}
]

lista_plac = [pracownik for pracownik in pracownicy if pracownik["stanowisko"] == "Specjalista"]

print(f"Oto nowa lista plac: {lista_plac}")
