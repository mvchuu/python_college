print("\t\nKalkulator Inwestycyjny\n")

kwota_poczatkowa = int(input("Wprowadz kwote inwetstycji: "))

cel = int(input("Ile pieniedzy chczesz posiadac koncowo: "))

roczne_oprocentowanie = float(input("Ile wynosi oprocentowanie(%): "))
roczne_oprocentowanie = 1+(roczne_oprocentowanie/100)
ilosc_lat = 0

while kwota_poczatkowa < cel:
    kwota_poczatkowa *= roczne_oprocentowanie
    ilosc_lat += 1

print(f"Po {ilosc_lat} lat zgromadzisz {kwota_poczatkowa}$")
