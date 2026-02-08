points = int(input("Podaj liczbe uzyskanych punktow: "))

ocena = 2.0

p = points

if p <= 100 and p >= 91:
    ocena = 5
elif p <= 90 and p >= 81:
    ocena = 4.5
elif p <= 80 and p >= 71:
    ocena = 4
elif p <= 70 and p >= 61:
    ocena = 3.5
elif p <= 60 and p >= 51:
    ocena = 3
else:
    pass

print(f"Otrzymujesz {ocena}.")
