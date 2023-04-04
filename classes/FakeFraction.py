import copy

class FakeFraction:
    def __init__(self, numo, deno):
        self.numo = numo
        self.deno = deno

    def getNum(self):
        return self.numo

    def getDeno(self):
        return self.deno

    def half(self):
        self.numo = self.numo // 2
        self.deno = self.deno // 2

    def __str__(self):
        return str(self.numo) + '/' + str(self.deno)

    def __add__(self, other_fraction):
        return FakeFraction(self.numo + other_fraction.numo,
                            self.deno + other_fraction.deno)

if __name__ == '__main__':
    frac1 = FakeFraction(1, 1)
    frac2 = FakeFraction(2, 2)
    frac3 = frac1 + frac2

    print(frac1)
    print(frac2)
    print(frac3)

    frac3.half()
    print(frac3)

    frac3.half()
    print(frac3)

    # shallow copy
    frac1_shallow_copy = copy.copy(frac1)
    print(frac1 is frac1_shallow_copy)
    print(frac1.deno is frac1_shallow_copy.deno)
    print(frac1.numo is frac1_shallow_copy.numo)

    frac1_deep_copy = copy.deepcopy(frac1)
    print(frac1 is frac1_deep_copy)
    print(frac1.deno is frac1_deep_copy.deno)
    print(frac1.numo is frac1_deep_copy.numo)
