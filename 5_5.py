class LicznikJednorazowy:
    def __init__(self, max_val):
        self.max_val = max_val
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < self.max_val:
            self.n += 1
            return self.n - 1
        else:
            raise StopIteration

licznik = LicznikJednorazowy(3)

for l in licznik:
    print(l)

for l in licznik:
    print(l)
