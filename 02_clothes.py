class Clothes:
    tissue_consumption = 0

    def __init__(self):
        pass


class Coat(Clothes):

    def __init__(self, size):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size < 40:
            self.__size = 40
        elif size > 65:
            self.__size = 65
        else:
            self.__size = size

    def plus(self):
        coat_cons = (self.size / 6.5 + 0.5)
        Clothes.tissue_consumption += coat_cons
        return coat_cons


class Costume(Clothes):

    def __init__(self, high):
        self.high = high

    @property
    def size(self):
        return self.__high

    @size.setter
    def size(self, high):
        if high < 140:
            self.__high = 140
        elif high > 220:
            self.__high = 220
        else:
            self.__high = high

    def plus(self):
        costume_cons = (2 * self.high + 0.3)
        Clothes.tissue_consumption += costume_cons
        return costume_cons


a = Coat(66)
b = Costume(270)
print(a.plus())
print(b.plus())
print(f'{a.tissue_consumption}')
