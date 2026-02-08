f = open("dziennik.txt", "w")
try:
    f.write("Pierwszy wpis.")
    f.write("\nWszystko dziala.")
finally:
    f.close()

f = open("dziennik.txt", "r")
try:
    odczyt = f.read()
finally:
    f.close()

print(odczyt)

f = open("dziennik.txt", "a")
try:
    f.write("\nDodaj nowa linie.")
finally:
    f.close()

f = open("dziennik.txt", "r")
try:
    odczyt_2 = f.read()
    print(odczyt_2)
finally:
    f.close()
