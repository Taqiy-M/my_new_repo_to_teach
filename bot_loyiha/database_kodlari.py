import sqlite3

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

con = sqlite3.connect("bazam.db")
kursor = con.cursor()
a = "AgACAgIAAxkBAAEXPvllRi5nu7dSd7fdO7Ld5oxlXn2dEgACd9YxGwgVMUpE9WOZG7liqQEAAwIAA3MAAzME"
b = "AgACAgIAAxkBAAEXPvtlRi5nYmr0hXyuUiR621kxdlt9WwACedYxGwgVMUokJqR028agQAEAAwIAA3MAAzME"
t = [a, b]

from random import choice

kursor.execute("""CREATE TABLE IF NOT EXISTS Category(
                    id INTEGER AUTO INCREMENT,
                    name TEXT,
                    rasm TEXT,
                    descr TEXT,
                    PRIMARY KEY (id));
                    """)

# kategoriya_nomlar = {
#     "Milliy Taomlar 🥣": "O\'zimizning milliy taomlarimizga nima yetsin! Osh bo\'lsin! Hammasi svejiy tayyrolangan.",
#     "Burgerlar 🍔": "Mazali tez tayyorlanuvchi yevropa taomlari.",
#     "Pizzalar 🍕": "Yumaloq pizzaga nima deysiz? Albatta HA!",
#     "Ichimliklar 🧃": "Chanqoqbosti muzdek va issiq ichimliklardan tanlang.",
#     "Shirinliklar 🍰": "Shirintomoqlar uchun maxsus!!",
#     "Saladlar 🥗": "Hazmi taom saladlar!"
# }
#
# for k, v in kategoriya_nomlar.items():
#     print(k, v)
#     kursor.execute(f"INSERT INTO Category (name, rasm, descr) VALUES (\"{k}\", \"{choice(t)}\",\"{v}\");")



def get_all_category_names():
    return kursor.execute("SELECT name FROM Category;")


def get_all_category_buttons():
    mrkp = ReplyKeyboardMarkup(resize_keyboard=True)
    for i in get_all_category_names():
        mrkp.add(KeyboardButton(i[0]))

    return mrkp






