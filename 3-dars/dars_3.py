class Human:
    def __init__(self, ism, yosh, vazn):
        self.ism = ism
        self.yosh = yosh
        self.vazn = vazn

    def speak(self):
        print("Assalomu alaykum! \nMen Human man")

    def move(self):
        print("Men oddiy Human yuryapman")


class Student(Human):
    def __init__(self, ism, yosh, vazn, univer, kurs):
        self.univer = univer
        self.kurs = kurs
        super().__init__(ism, yosh, vazn)


    def speak(self):
        super().speak()
        print(f"Salom! Men {self.kurs}-kursman. Ismim {self.ism}")

    def move(self):
        print("Talaba harakatlanyapti.")



def h(a):
    a.speak()




# a = Student("Abdulloh", 20, 62, "TATU", 2)
# a.speak()


# encapsulation

class Human:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh
        self._parol = 404

    def _hello(self):
        print("Salommmm")



class Student(Human):
    def __init__(self, ism, yosh, univer):
        self.univer = univer
        super().__init__(ism, yosh)
        super()._hello()

# b = Human("BBB", 22)
# b._hello()
# print(b.parol)
# a = Student("a", 1, "T")
# print(a.parol)

class Car:
    def __init__(self, name, year, price, max_speed):
        self.name = name
        self.year = year
        self.price = price
        self.max_speed = max_speed
        self.__speed = 0
        self.__started = False

    def _show(self):
        print(f"Mashina: {self.name}.\n"
              f" {self.year} yilda chiqqan"
              f"\n")
        print(f"Narxi: {self.price}")

    def set_tezlik(self, a=10):
        if self.__started:
            if self.__speed+a <= self.max_speed:
                self.__speed += a
            else:
                self.__speed = self.max_speed

    def get_tezlik(self):
        return self.__speed

    def start(self):
        self.__started = True
        print(f"{self.name} yondi")

    def show_speed(self):
        print(self.__speed)

# mcquin = Car("Mcquin", 2004, 400000, 350)
# mcquin.start()
# mcquin.set_tezlik(100)
# mcquin.set_tezlik()
# mcquin.set_tezlik()
# print(mcquin)
# mcquin.start()
# mcquin.tezlashish()
# mcquin.tezlashish(400)
# mcquin.tezlashish(400)
# mcquin.tezlashish(400)
# mcquin.tezlashish(400)
# mcquin.tezlashish(400)
# mcquin.show_speed()
# setter
# getter

















