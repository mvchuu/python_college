def znajdz_wartosc(dane, szukany_klucz):
    for klucz, wartosc in dane.items():
       if klucz == szukany_klucz:
           return wartosc
       if isinstance(wartosc, dict):
           znaleziona_wartosc = znajdz_wartosc(wartosc, szukany_klucz)
           if znaleziona_wartosc is not None:
               return znaleziona_wartosc
    
    return None

konfiguracja = {
	"uzytkownik": "admin", 
    "baza_danych": {
		"host": "localhost",
        "port": 5432, 
        "credentials": {
			"user": "db_user", 
            "password": "secret_password" 
			}
		}
	}

haslo = znajdz_wartosc(konfiguracja, "password")
print(f"Znalezione hasło: {haslo}")
