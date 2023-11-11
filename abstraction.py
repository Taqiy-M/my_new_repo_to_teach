# E-commerce Platform:
# Create a sophisticated e-commerce platform
# with classes for User, Product,
# ShoppingCart, and Order.
# Users can be both customers and sellers.
# Implement an intricate order processing system,
# with multiple payment methods and shipping options.
# Apply encapsulation to secure user and payment information.
from products import Cloth, Gadget
from users import User
from orders import Cart, Order

a = Cloth("T-Shirt f178", 46, "Tommy Hilfiger",
          2023,
          "Lorem ipsum akjsfaleijfaliskjdflksajflkjeif", "L", "Oversize")
b = Cloth("T-Shirt f178", 50, "Tommy Hilfiger",
          2023,
          "Lorem ipsum akjsfaleijfaliskjdflksajflkjeif", "XL", "Oversize")
c = Cloth("T-Shirt f178", 42, "Tommy Hilfiger",
          2023,
          "Lorem ipsum akjsfaleijfaliskjdflksajflkjeif",
          "M", "Oversize")
u = User("Orifjon Solijonov", 2007,
         "AD3910324", "99 998 77 89",
         "Qirguli MFY, Marifat 19")
v = User("Hojimurod Solijonov", 2006,
         "AC3910324", "99 998 77 89",
         "Bag'dod tumani, Marifat 19")


w = Cart(1, "Pending", u)
o = Order(a, 4, w)
o1 = Order(b, 2, w)
o3 = Order(c, 3, w)
w._Cart__holat = "Completed"
print(w.get_narx())
print(w.get_holat())
print(u.get_ism())










