# import sqlite3
# a = sqlite3.connect('mening_bazam.db')
# kursor = a.cursor()
# kursor.execute("SELECT * FROM City")
# kursor.execute("ALTER TABLE Student RENAME TO Talaba")

# kursor.fetchone()
# kursor.fetchone()
# kursor.fetchmany(10)
# print(kursor.fetchmany(10))








# res = kursor.fetchall()

# for i in res:
#     print(i)


# while True:
#     c = kursor.fetchone()
#     if c is None:
#         break
#     print(c)






a.commit()
a.close()














# import mysql.connector
#
# # Database connection parameters
# db_config = {
#     "host": "localhost",
#     "user": "root",
#     "password": "qwerty12345",
#     "database": "mening_bazam"
# }
#
# conn = mysql.connector.connect(**db_config)

# conn = mysql.connector.connect(
#     host="localhost",
#     database="mening_bazam",
#     user="root",
#     password="qwerty12345")
