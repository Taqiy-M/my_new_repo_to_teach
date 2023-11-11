class Human:
    def __init__(self, name, year, city, height, weight):
        self.city = city
        self.year = year
        self.name = name
        self.height = height
        self.weight = weight


    def show(self):
        print(f"Name: {self.name}")
        print(f"Year: {self.year}")
        print(f"City: {self.city}")
        print(f"Height: {self.height}")
        print(f"Weight: {self.weight}")

# a = Human(year = 2007, shahar="Marg'ilon", name="Ali")
# b = Human("Ahrorjon", 2001, "Bag'dod")


class Student(Human):
    def __init__(self, name, year, city, height, weight, univer, grade):
        super().__init__(name, year, city, height, weight)
        self.grade = grade
        self.univer = univer

    def show(self):
        super().show()
        print(f"Universitet: {self.univer}")
        print(f"Kurs: {self.grade}")

    def __repr__(self):
        return self.name + " " + self.city + " " + self.univer

    def __gt__(self, other):
        return self.grade > other.grade

    def __ge__(self, other):
        return self.grade >= other.grade

    def __eq__(self, other):
        return self.grade == other.grade

    def __add__(self, other):
        if isinstance(other, int):
            return self.weight+other
        return self.weight + other.weight


a = Student("Ahmadali", 2002, "Bag'dod", 176, 60, "TATU", 3)
b = Student("Mahmudali", 2000, "Qarshi", 169, 80, "FarDU", 2)
# print(a > b)
# a.show()
# print(b)
# print(a+40)

# a == b




# def hello(a=1, b=1):
#     for i in range(0, a, b):
#         print(f"{i} Assalomu alaykum")
# hello(20)
# hello(20, 2)
# hello()
# class English:
#     def speak(self):
#         print("'Mornin...")
#
# class Uzbek:
#     def speak(self):
#         print("Salom...")
#
# class Turkish:
#     def speak(self):
#         print("Merhaba")
#
# class Chinese:
#     def speak(self):
#         print("Nihao")


# def salom(a):
#     a.speak()
#
#
#
# y = Chinese()
# salom(y)





class Car:
    def __init__(self, name, brend, price, color, max_speed, year):
        self.year = year
        self.max_speed = max_speed
        self.color = color
        self.price = price
        self.brend = brend
        self.name = name
        self.__speed = 0

    def start(self):
        print("G'nnn.. ")

    def get_speed(self):
        return self.__speed

    def tezlash(self, a=10):
        if self.__speed + a <=self.max_speed:
            self.__speed += a
        else:
            self.__speed = self.max_speed

# a = Car("Nexia 3", "Ravon", 7000, "Qizil", 220, 2021)
# a.tezlash()
# a.tezlash(20)
# a.tezlash(130)
# a.tezlash(150)
# print(a.get_speed())





from abc import ABC, abstractmethod

class Car(ABC):

    @property
    @abstractmethod
    def speed(self):
        pass


    @abstractmethod
    def start(self):
        pass


class Audi(Car):
    sp = 0

    @property
    def speed(self):
        return self.sp

    @speed.setter
    def speed(self, a):
        self.sp += a

    def start(self):
        print("Salomat!!!!!!!!")


# a = Audi()
# a.speed = 20
# a.speed = 20
# a.speed = 20
# print(a.speed)





from datetime import datetime, date, time

# print(datetime.today())
# print(date.today())
# print(date.today().weekday())

# sana = date(2008, 4, 8)
# date.today().weekday()
# print(sana.weekday())
# e = date.today()-date(1997, 11, 10)
# print(e.total_seconds()/60/60/24/365)

# 21.10.2023, Saturday

# print(sana.strftime("%-d-%B, %Y"))
# "4-January, 2020"
# st1 = "21-January, 2020"
# st2 = "11-March, 1970"
# form = "%d-%B, %Y"
# date1 = datetime.strptime(st1, form)
# date2 = datetime.strptime(st2, form)
# print((date1-date2).total_seconds()/60/60/24/30)



import _thread


def sanamoq(id, a):
    for i in range(a+1):
        print(f"{id}===========>{i}")


# _thread.start_new_thread(sanamoq, (1, 100))
# _thread.start_new_thread(sanamoq, (2, 100))
# _thread.start_new_thread(sanamoq, (3, 100))
# _thread.start_new_thread(sanamoq, (4, 100))
# _thread.start_new_thread(sanamoq, (5, 100))
# input()
# while True:
#     print("Ramazon muborak")
























