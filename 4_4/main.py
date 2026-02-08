class NiepoprawnaIloscProduktuError(ValueError):
    pass    

def dodaj_do_koszyka(produkt, ilosc):
    if ilosc <= 0:
        raise NiepoprawnaIloscProduktuError("Ilosc produktu musi byc dodatnia!")


try:
    dodaj_do_koszyka("Bulka", 2)
    dodaj_do_koszyka("Bulka", -3)
except NiepoprawnaIloscProduktuError as e:
    print(e)
