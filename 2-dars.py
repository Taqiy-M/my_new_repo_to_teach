class Car:
    def __init__(self, narx, brend, rang, yil, maks_tezlik):
        self.tezlik = 0
        self.harakatda = False
        self.maks_tezlik = maks_tezlik
        self.yil = yil
        self.rang = rang
        self.brend = brend
        self.narx = narx

    def start(self):
        if not self.harakatda:
            self.harakatda = True
            print("Mashina yondi")

        else:
            print("Kalitti sindirvorasiz, burormeng")

    def stop(self):
        if self.harakatda:
            self.harakatda = False
            print("Mashina o'chdi.")
        else:
            print("Hay hay kalit sinadiya.")

    def sekinlash(self):
        pass

    def tezlash(self, a=5):
        if self.tezlik+a < self.maks_tezlik:
            self.tezlik += a
            print(f"Hozirgi tezlik: {self.tezlik}")
        else:
            self.tezlik = self.maks_tezlik
            print("Mashina maksimal tezlikka erishgan")
            print(f"Hozirgi tezlik: {self.tezlik}")

# a = Car(2000, "Nexia-3", "Sariq", 2008, 220)
# a.start()
# a.tezlash(1000)

# polimorfizm
# polymorphism

# method overloading
# method overriding
# operator overloading
# duck typing


# method overloading
# def sum(a=0, b=0, c=0, d=0, e=0):
#     print(a+b+c+d+e)
# sum(8, 9)
# sum(8, 9, 1)
# sum(100)

# a = "Hello"
# b = ["assalomu", "alaykum"]
# d = {
#     "1": "Salom",
#     0: "Ehheee",
#     3: 3245466
# }

# print(len(a))


# print(1*10)
# print("1"*10)
# print(False and 1)
# print("salom" > "999932234")
# print(1 > 2)


class Dog:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Vov-Vov-vovovov")

class Cat:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Myau-myau-mov-myau")


def say(a):
    a.speak()


# h = Dog("Olapar")
# g = Cat("Tom")
# say(h)


# class Uzbek:
#     def hello(self):
#         print("Assalomaleykum brat.")
# class English:
#     def hello(self):
#         print("Hello, bro")
# class Chinese:
#     def hello(self):
#         print("Nihao, shi")
# def intro(odam):
#     odam.hello()
#
# ali = English()
# intro(ali)

import _thread
import turtle


class Shape:
    def __init__(self, size, color, shape, speed, x, y):
        self.t = turtle.Turtle()
        self.t.pensize(size)
        self.t.color(color)
        self.t.shape(shape)
        self.t.speed(speed)
        self.t.up()
        self.t.goto(x, y)
        self.t.down()

    def chiz(self):
        raise NotImplementedError("chiz metodi yartilmagan!!!")



class Square(Shape):
    def __init__(self, size, color, shape, speed, x, y):
        super().__init__(size, color, shape, speed, x, y)


    def chiz(self, a):
        # self.t.fillcolor("green")
        # self.t.begin_fill()
        for i in range(4):
            self.t.fd(a)
            self.t.right(90)
        self.t.end_fill()


class Circle(Shape):
    def __init__(self, size, color, shape, speed, x, y):
        super().__init__(size, color, shape, speed, x, y)

    def chiz(self, a):
        self.t.circle(a)

class Triangle(Shape):
    def __init__(self, size, color, shape, speed, x, y):
        super().__init__(size, color, shape, speed, x, y)

    def chiz(self, a):
        for i in range(3):
            self.t.fd(a)
            self.t.left(120)
# thread


# a = Square(10, "Red", "circle", 3, -400, 500)
# b = Circle(10, "Green", "turtle", 3, 350, -450)
# c = Triangle(10, "Cyan", "square", 3, -400, -500)
# _thread.start_new_thread(a.chiz, (1000,))
# _thread.start_new_thread(b.chiz, (300, ))
# _thread.start_new_thread(c.chiz, (300, ))

# turtle.done()




class Student:
    def __init__(self, name, year, grade, gpa, univer):
        self.name = name
        self.year = year
        self.grade = grade
        self.gpa = gpa
        self.univer = univer


    def show(self):
        print("Assalomu alaykum!")
        print(f"Mening ismim {self.name}")
        print(f"Mening yoshim {2023-self.year}")
        print(f"{self.grade} kursda o'qiyman. Bahoim {self.gpa}")

    def __str__(self):
        self.show()
        return self.name

    def __repr__(self):
        return self.name

    def __add__(self, other):
        self.grade += int(other)
        print(f"Ahmad endi {self.grade} - kursga o'tdi")
        return self.grade

    def __ge__(self, other):
        if isinstance(other, Student):
            return self.year <= other.year
        else:
            return self.year < other

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.year < other.year
        else:
            return self.year < other

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.year == other.year
        else:
            return self.year == other

    def __len__(self):
        return len(self.name)


a = Student("Ahmad", 1997, 1, 4.2, "INHA")
b = Student("Jamshid", 1999, 4, 2.7, "TATU")
c = Student("Jobir", 1995, 2, 4, "FarDU")
d = Student("Umid", 2003, 3, 3.5, "ToshMI")

# l = [a, b, c, d]
# l.sort()
# print(l)
# print(a != b)
# print(a <= 1998)
# print(len(a))
# print(len(b))







