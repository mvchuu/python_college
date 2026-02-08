import csv

sprzedaz = [
        {"produkt":"zupa", "sprzedana_ilosc":10, "przychody":100},
        {"produkt":"ogorek", "sprzedana_ilosc":40, "przychody":500}
]

def zapisz_raport_sprzedazy(sciezka:str, dane:list):
    if dane:
        nazwy_kolumn = dane[0].keys()
        
        with open(sciezka, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=nazwy_kolumn)
            writer.writeheader()
            writer.writerows(dane)
    else:
        return f"BLAD: Lista jest pusta!"


zapisz_raport_sprzedazy("raport.csv", sprzedaz)
