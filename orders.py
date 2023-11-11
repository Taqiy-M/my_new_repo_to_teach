class Order:
    def __init__(self, product, amount, cart):
        self.__cart = cart
        self.__amount = amount
        self.__product = product
        self.__cart.set_narx(amount*product.get_narx())


class Cart:
    def __init__(self, id, holat, user):
        self.__user = user
        self.__holat = holat
        self.__id = id
        self.__narx = 0
        self.__bonus = 0

    def get_narx(self):
        print(f"Narx: {self.__narx}\nBonus:{self.__bonus}")
        return self.__narx-self.__bonus

    def set_narx(self, a):
        self.__narx += a
        self.__bonus += a/40


    def get_user(self):
        return self.__user.get_ism()

    def get_holat(self):
        return self.__holat

    def get_id(self):
        return self.__id





