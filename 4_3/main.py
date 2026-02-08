with open("dziennik.txt", "w") as f:
    f.write("Pierwszy wpis.\n")
    f.write("Wszystko dziala.\n")

with open("dziennik.txt", "a") as f:
    f.write("Dodano kolejna linijke.\n")

with open("dziennik.txt", "r") as f:
    odczyt = f.read()
    print(odczyt)
