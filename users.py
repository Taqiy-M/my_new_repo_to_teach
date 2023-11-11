class User:
    def __init__(self, fish, yil, passport, telefon, manzil):
        self.__manzil = manzil
        self.__telefon = telefon
        self.__passport = passport
        self.__yil = yil
        self.__fish = fish

    def get_manzil(self):
        return self.__manzil

    def get_telefon(self):
        return self.__telefon

    def get_ism(self):
        return self.__fish

    def get_passport(self):
        return self.__passport

    def get_yil(self):
        return self.__yil








d = {}
while True:
    a = input()
    if a == "-1":
        break
    if d.get(a) is None:
        d[a] = 1
    else:
        d[a] += 1

for k, v in d.items():
    print(k, v)









