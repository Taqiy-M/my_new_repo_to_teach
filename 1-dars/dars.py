



class Talaba:
    id = 0
    ism = "Ahmad"
    year = 2005
    univer = "TATU"
    shahar = "Farg'ona"


# object == instance
# s = Talaba()
# s.ism = "Jamshid"
# print(s.ism, s.year)


class Talaba:
    def __init__(self, id, ism, year, univer, shahar):
        self.id = id
        self.ism = ism
        self.year = year
        self.univer = univer
        self.shahar = shahar


    def show(self):
        print(f"Assalomu alaykum! Mening ismim {self.ism}. Yoshim {2023-self.year}da")
        print(f"Hozirda {self.univer}da o'qiyman. Lekin o'zim {self.shahar}danman")

    def salom(self, a):
        print(a, "argument sifatida kiritildi.")
        self.ism = "Ali"
        print(f"Assalomu alaykum {self.ism}")

    def ask_money(self):
        print(f"Assalomu alaykum. Man, {self.ism}man yaxshi o'tiribsilarmi. "
              "Qiynalmayapsilarmi "
              "Manam shu o'qib yurippan, kecha tushimga kirippopsilar. "
              "shunga xabar ogani qilodim. Ish - pish bo'pposa aytorilar "
              "telefonam qibturilar orada odam puli bo'masa qiyinakan.")

    def hayol(self):
        print(f"Hammayo'q buzuqlik bo'pketipti shahrda."
              f" Man yo'q jaa quyish qonidan chiqketipsilar. "
              f"Kontrakt qimmatlashyapti dollar qurg'ur o'ynayapti"
              f"Puliyam o'lsin. Yosham {2023-self.year+5} ga qarab ketyapti"
              f"Ehhh. Uylanish kerak... Salimboyni qizi bormikin...")


# a = Talaba(1, "Alimuhammad", 2006, "FarDU", "Farg'ona")
# b = Talaba(2, "Ahmadali", 2001, "TATU", "Farg'ona")
# c = Talaba(3, "Jamshid", 1999, "INHA", "Farg'ona")
# d = Talaba(4, "Abduxoliq", 1997, "HAYOT", "Farg'ona")
# e = Talaba(5, "Hojimurod", 2007, "ToshMI", "Farg'ona")
# a.show()
# e.show()


# inheritance ==   is-a  relationship

class Hayvon:
    def __init__(self, ism, yil, jins):
        self.ism = ism
        self.yil = yil
        self.jins = jins


class SutEmizuvchi(Hayvon):
    def __init__(self, qol=4, tezlik="20 kmh"):
        self.qol = qol
        self.tezlik = tezlik
        Hayvon.__init__(self, "Gomish", 2000, "Male")


    def show(self):
            print("Assalooom.")
            print("Muuuuuu... Muuuu.... Muuuuzdek ekan")



class Mol(SutEmizuvchi):
    def __init__(self, sut, kg):
        self.sut = sut
        self.kg = kg
        SutEmizuvchi.__init__(self, qol=4, tezlik="20 km/h")


# a = Mol(5, 300)
# print(a.yil)

# class Ota:
#     def __init__(self, ism, yosh):
#         self.o_ism = ism
#         self.o_yosh = yosh
#
#     def show(self):
#         print("Men ota bo'ldim!!!")
#
#
# class Bola(Ota):
#     def __init__(self):
#         print("Ingaa")



# a = Bola()
# a.show()

# a = Talaba()
# a.salom("Heheheee")


# b = Talaba()
# b.salom()
# print(b.ism)
# b.ask_money()
# b.hayol()


# parent class yoki base class
# child class derived class

# constructor == klassdan obyekt olingan paytda ishga tushib ketadigan
# funksiya constructor deyiladi
# destructor  == obyekt o'chib ketgan paytda ishga tushib ketadigan
# funksiya destructor


# class Shakl:
#     yuza = 0
#     uzunlik = 0
#     burchak = 0
#
#
# class Kvadrat(Shakl):
#     def __init__(self):
#         pass
#
#
# class Uchburchak():
#     pass























