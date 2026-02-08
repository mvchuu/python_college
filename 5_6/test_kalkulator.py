import dodaj from kalkulator

def test_dodawania_liczb_dodatnich():
    assert dodaj(2, 3) == 5

def test_dodawania_liczb_ujemnych():
    assert dodaj(-3, -5) == -8
