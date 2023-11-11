from abc import ABC, abstractmethod


class Product(ABC):
    def __init__(self, nom, narx, brend, yil, batafsil):
        self._batafsil = batafsil
        self._yil = yil
        self._brend = brend
        self._narx = narx
        self._nom = nom

    @abstractmethod
    def get_nom(self):
        pass

    @abstractmethod
    def get_yil(self):
        pass

    @abstractmethod
    def get_narx(self):
        pass

    @abstractmethod
    def get_brend(self):
        pass

    @abstractmethod
    def get_batafsil(self):
        pass


class Cloth(Product):
    def __init__(self, nom, narx, brend, yil, batafsil, size, style):
        self._size = size
        self._style = style
        super().__init__(nom, narx, brend, yil, batafsil)

    def get_nom(self):
        return self._nom

    def get_narx(self):
        return self._narx

    def get_yil(self):
        return self._yil

    def get_brend(self):
        return self._brend

    def get_batafsil(self):
        return self._batafsil


class Gadget(Product):
    def __init__(self, nom, narx, brend, yil,
                 batafsil, type, is_second_hand):
        super().__init__(nom, narx, brend, yil, batafsil)
        self._is_second_hand = is_second_hand
        self._type = type

    def get_is_second_hand(self):
        return self._is_second_hand

    def get_type(self):
        return self._type

    def get_nom(self):
        return self._nom

    def get_narx(self):
        return self._narx

    def get_yil(self):
        return self._yil

    def get_brend(self):
        return self._brend

    def get_batafsil(self):
        return self._batafsil

