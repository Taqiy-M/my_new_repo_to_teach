# # from PyQt5.QtWidgets import *
# #
# # app = QApplication([])
#
# # class Window(QMainWindow):
# #     def __init__(self):
# #         super().__init__()
# #         self.i = 10
# #         self.setWindowTitle("Saidamirxon")
# #         # le = QLineEdit()
# #         # le.textChanged.connect(self.le_edited)
# #         self.btn = QPushButton("10")
# #         self.btn.clicked.connect(self.btn_clicked)
# #         self.setCentralWidget(self.btn)
# #
# #     def btn_clicked(self):
# #         self.i -= 1
# #         self.btn.setText(f"{self.i}")
# #         if self.i == 0:
# #             self.btn.setEnabled(False)
# #
# #
# #     def le_edited(self, a):
# #         print(a)
# #
# #     def mousePressEvent(self, a0):
# #         pass
# #
# #     def mouseDoubleClickEvent(self, a0):
# #         pass
# #
# #     def mouseReleaseEvent(self, a0):
# #         pass
# #
# #
# #
# # class Windows(QMainWindow):
# #     def __init__(self):
# #         super().__init__()
# #
# #
# #
# # b = Windows()
# # b.show()
#
# # a = QPushButton("Bir")
# # a.show()
# # b = QLabel("Ikki")
# # b.show()
# # c = QSlider()
# # c.show()
# # d = QLineEdit()
# # d.show()
# # e = QTextEdit()
# # e.show()
# # app.exec()
#
#
#
# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import QPalette, QColor
# app = QApplication([])
#
#
#
# l = ['red', 'green', 'cyan', 'yellow', 'black', 'white', 'blue', 'orange', 'magenta']
# from random import choice
#
#
# # class MainWindow(QMainWindow):
# #     def __init__(self):
# #         super(MainWindow, self).__init__()
# #         self.setAutoFillBackground(True)
# #         self.setWindowTitle("My App")
# #         self.b = QPushButton("Click Me")
# #         self.b.clicked.connect(self.btn_clicked)
# #         self.setCentralWidget(self.b)
#
#
#
#     # def btn_clicked(self):
#     #     r = choice(l)
#     #     palette = self.palette()
#     #     palette.setColor(QPalette.Button, QColor(r))
#     #     self.b.setAutoFillBackground(True)
#     #     self.b.setPalette(palette)
#
#
#
# class Color(QWidget):
#     def __init__(self, color):
#         super().__init__()
#         self.setAutoFillBackground(True)
#         palette = self.palette()
#         palette.setColor(QPalette.Window, QColor(color))
#         self.setPalette(palette)
#
#
# # c = Color("green")
# # c.show()
#
#
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         # v_lay = QHBoxLayout()
#
#         # a = QPushButton("First Button")
#         # b = QPushButton("Second Button")
#         # c = QPushButton("Third Button")
#         # d = QPushButton("Done Button.")
#         # v_lay.addWidget(a)
#         # v_lay.addWidget(b)
#         # v_lay.addWidget(c)
#         # v_lay.addWidget(d)
#         # w = QWidget()
#         # w.setLayout(v_lay)
#         # self.setCentralWidget(w)
#         # layout1 = QVBoxLayout()
#         # layout2 = QHBoxLayout()
#         # layout3 = QHBoxLayout()
#         #
#         # layout2.addWidget(Color('red'))
#         # layout2.addWidget(Color('yellow'))
#         # layout2.addWidget(Color('purple'))
#         #
#         # layout1.addLayout(layout2)
#         #
#         # layout1.addWidget(Color('green'))
#         # layout3.addWidget(Color('red'))
#         # layout3.addWidget(Color('purple'))
#         #
#         # layout1.addLayout(layout3)
#         #
#         # widget = QWidget()
#         # widget.setLayout(layout1)
#         # self.setCentralWidget(widget)
#         layout = QGridLayout()
#
#         layout.addWidget(Color('red'), 0, 3)
#         layout.addWidget(Color('green'), 1, 1)
#         layout.addWidget(Color('blue'), 2, 2)
#         layout.addWidget(Color('purple'), 3, 0)
#         widget = QWidget()
#         widget.setLayout(layout)
#         self.setCentralWidget(widget)
#
#
# from PyQt5.QtWidgets import QStackedLayout  # add this import
#
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("My App")
#
#         layout = QStackedLayout()
#
#         layout.addWidget(Color("red"))
#         layout.addWidget(Color("green"))
#         layout.addWidget(Color("blue"))
#         layout.addWidget(Color("yellow"))
#
#         layout.setCurrentIndex(1)
#
#         widget = QWidget()
#         widget.setLayout(layout)
#         self.setCentralWidget(widget)
#
# import sys
#
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import (
#     QApplication,
#     QHBoxLayout,
#     QLabel,
#     QMainWindow,
#     QPushButton,
#     QStackedLayout,
#     QVBoxLayout,
#     QWidget,
# )
#
#
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         a = Color("magenta")
#         b = Color('cyan')
#         c = Color('black')
#         d = Color('purple')
#         e = Color('violet')
#         self.v = QVBoxLayout()
#         self.v.addWidget(a)
#         self.v.addWidget(b)
#         self.v.addWidget(c)
#         self.v.addWidget(d)
#         self.v.addWidget(e)
#
#         self.setWindowTitle("My App")
#         self.eng_kotta = QHBoxLayout()
#         pagelayout = QVBoxLayout()
#         self.eng_kotta.addLayout(self.v)
#         self.eng_kotta.addLayout(pagelayout)
#         button_layout = QHBoxLayout()
#         self.stacklayout = QStackedLayout()
#
#         pagelayout.addLayout(button_layout)
#         pagelayout.addLayout(self.stacklayout)
#
#         btn = QPushButton("red")
#         btn.pressed.connect(self.activate_tab_1)
#         button_layout.addWidget(btn)
#         self.stacklayout.addWidget(Color("red"))
#
#         btn = QPushButton("green")
#         btn.pressed.connect(self.activate_tab_2)
#         button_layout.addWidget(btn)
#         self.stacklayout.addWidget(Color("green"))
#
#         btn = QPushButton("yellow")
#         btn.pressed.connect(self.activate_tab_3)
#         button_layout.addWidget(btn)
#         self.stacklayout.addWidget(Color("yellow"))
#
#         widget = QWidget()
#         widget.setLayout(self.eng_kotta)
#         self.setCentralWidget(widget)
#
#     def activate_tab_1(self):
#         self.stacklayout.setCurrentIndex(0)
#
#     def activate_tab_2(self):
#         self.stacklayout.setCurrentIndex(1)
#
#     def activate_tab_3(self):
#         self.stacklayout.setCurrentIndex(2)
#

# from PyQt5.QtWidgets import *
# app = QApplication([])
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
        # a = QVBoxLayout()
        # self.b = QPushButton("Enter")
        # self.b.setEnabled(False)
        # c = QCheckBox("Yes, I am older 18")
        # c.stateChanged.connect(self.c_checked)
        # a.addWidget(c)
        # a.addWidget(self.b)
        # w = QWidget()
        # w.setLayout(a)
        # self.setCentralWidget(w)

        # widget = QComboBox()
        # widget.addItems(["Uzbekistan", "USA", "Ukraine", "Palestine", "Egypt"])
        # widget.setEditable(True)
        # widget.setInsertPolicy(QComboBox.InsertAlphabetically)
        # widget.currentIndexChanged.connect(self.index_changed)
        # widget.currentTextChanged.connect(self.text_changed)
        # self.setCentralWidget(widget)


#     def index_changed(self, a):
#         print(f"Index o'zgardi: {a}")
#
#
#     def text_changed(self, a):
#         print(f"Text o'zgardi: {a}")
#
#
#     def c_checked(self, e):
#         self.b.setEnabled(e)
#
#
# window = MainWindow()
# window.show()
# app.exec()
import qrcode as qrcode

# # from PyQt5.QtWidgets import *
# #
# # app = QApplication([])
#
# # class Window(QMainWindow):
# #     def __init__(self):
# #         super().__init__()
# #         self.i = 10
# #         self.setWindowTitle("Saidamirxon")
# #         # le = QLineEdit()
# #         # le.textChanged.connect(self.le_edited)
# #         self.btn = QPushButton("10")
# #         self.btn.clicked.connect(self.btn_clicked)
# #         self.setCentralWidget(self.btn)
# #
# #     def btn_clicked(self):
# #         self.i -= 1
# #         self.btn.setText(f"{self.i}")
# #         if self.i == 0:
# #             self.btn.setEnabled(False)
# #
# #
# #     def le_edited(self, a):
# #         print(a)
# #
# #     def mousePressEvent(self, a0):
# #         pass
# #
# #     def mouseDoubleClickEvent(self, a0):
# #         pass
# #
# #     def mouseReleaseEvent(self, a0):
# #         pass
# #
# #
# #
# # class Windows(QMainWindow):
# #     def __init__(self):
# #         super().__init__()
# #
# #
# #
# # b = Windows()
# # b.show()
#
# # a = QPushButton("Bir")
# # a.show()
# # b = QLabel("Ikki")
# # b.show()
# # c = QSlider()
# # c.show()
# # d = QLineEdit()
# # d.show()
# # e = QTextEdit()
# # e.show()
# # app.exec()
#
#
#
# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import QPalette, QColor
# app = QApplication([])
#
#
#
# l = ['red', 'green', 'cyan', 'yellow', 'black', 'white', 'blue', 'orange', 'magenta']
# from random import choice
#
#
# # class MainWindow(QMainWindow):
# #     def __init__(self):
# #         super(MainWindow, self).__init__()
# #         self.setAutoFillBackground(True)
# #         self.setWindowTitle("My App")
# #         self.b = QPushButton("Click Me")
# #         self.b.clicked.connect(self.btn_clicked)
# #         self.setCentralWidget(self.b)
#
#
#
#     # def btn_clicked(self):
#     #     r = choice(l)
#     #     palette = self.palette()
#     #     palette.setColor(QPalette.Button, QColor(r))
#     #     self.b.setAutoFillBackground(True)
#     #     self.b.setPalette(palette)
#
#
#
# class Color(QWidget):
#     def __init__(self, color):
#         super().__init__()
#         self.setAutoFillBackground(True)
#         palette = self.palette()
#         palette.setColor(QPalette.Window, QColor(color))
#         self.setPalette(palette)
#
#
# # c = Color("green")
# # c.show()
#
#
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         # v_lay = QHBoxLayout()
#
#         # a = QPushButton("First Button")
#         # b = QPushButton("Second Button")
#         # c = QPushButton("Third Button")
#         # d = QPushButton("Done Button.")
#         # v_lay.addWidget(a)
#         # v_lay.addWidget(b)
#         # v_lay.addWidget(c)
#         # v_lay.addWidget(d)
#         # w = QWidget()
#         # w.setLayout(v_lay)
#         # self.setCentralWidget(w)
#         # layout1 = QVBoxLayout()
#         # layout2 = QHBoxLayout()
#         # layout3 = QHBoxLayout()
#         #
#         # layout2.addWidget(Color('red'))
#         # layout2.addWidget(Color('yellow'))
#         # layout2.addWidget(Color('purple'))
#         #
#         # layout1.addLayout(layout2)
#         #
#         # layout1.addWidget(Color('green'))
#         # layout3.addWidget(Color('red'))
#         # layout3.addWidget(Color('purple'))
#         #
#         # layout1.addLayout(layout3)
#         #
#         # widget = QWidget()
#         # widget.setLayout(layout1)
#         # self.setCentralWidget(widget)
#         layout = QGridLayout()
#
#         layout.addWidget(Color('red'), 0, 3)
#         layout.addWidget(Color('green'), 1, 1)
#         layout.addWidget(Color('blue'), 2, 2)
#         layout.addWidget(Color('purple'), 3, 0)
#         widget = QWidget()
#         widget.setLayout(layout)
#         self.setCentralWidget(widget)
#
#
# from PyQt5.QtWidgets import QStackedLayout  # add this import
#
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("My App")
#
#         layout = QStackedLayout()
#
#         layout.addWidget(Color("red"))
#         layout.addWidget(Color("green"))
#         layout.addWidget(Color("blue"))
#         layout.addWidget(Color("yellow"))
#
#         layout.setCurrentIndex(1)
#
#         widget = QWidget()
#         widget.setLayout(layout)
#         self.setCentralWidget(widget)
#
# import sys
#
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import (
#     QApplication,
#     QHBoxLayout,
#     QLabel,
#     QMainWindow,
#     QPushButton,
#     QStackedLayout,
#     QVBoxLayout,
#     QWidget,
# )
#
#
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         a = Color("magenta")
#         b = Color('cyan')
#         c = Color('black')
#         d = Color('purple')
#         e = Color('violet')
#         self.v = QVBoxLayout()
#         self.v.addWidget(a)
#         self.v.addWidget(b)
#         self.v.addWidget(c)
#         self.v.addWidget(d)
#         self.v.addWidget(e)
#
#         self.setWindowTitle("My App")
#         self.eng_kotta = QHBoxLayout()
#         pagelayout = QVBoxLayout()
#         self.eng_kotta.addLayout(self.v)
#         self.eng_kotta.addLayout(pagelayout)
#         button_layout = QHBoxLayout()
#         self.stacklayout = QStackedLayout()
#
#         pagelayout.addLayout(button_layout)
#         pagelayout.addLayout(self.stacklayout)
#
#         btn = QPushButton("red")
#         btn.pressed.connect(self.activate_tab_1)
#         button_layout.addWidget(btn)
#         self.stacklayout.addWidget(Color("red"))
#
#         btn = QPushButton("green")
#         btn.pressed.connect(self.activate_tab_2)
#         button_layout.addWidget(btn)
#         self.stacklayout.addWidget(Color("green"))
#
#         btn = QPushButton("yellow")
#         btn.pressed.connect(self.activate_tab_3)
#         button_layout.addWidget(btn)
#         self.stacklayout.addWidget(Color("yellow"))
#
#         widget = QWidget()
#         widget.setLayout(self.eng_kotta)
#         self.setCentralWidget(widget)
#
#     def activate_tab_1(self):
#         self.stacklayout.setCurrentIndex(0)
#
#     def activate_tab_2(self):
#         self.stacklayout.setCurrentIndex(1)
#
#     def activate_tab_3(self):
#         self.stacklayout.setCurrentIndex(2)
#

# from PyQt5.QtWidgets import *
# app = QApplication([])
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
        # a = QVBoxLayout()
        # self.b = QPushButton("Enter")
        # self.b.setEnabled(False)
        # c = QCheckBox("Yes, I am older 18")
        # c.stateChanged.connect(self.c_checked)
        # a.addWidget(c)
        # a.addWidget(self.b)
        # w = QWidget()
        # w.setLayout(a)
        # self.setCentralWidget(w)

        # widget = QComboBox()
        # widget.addItems(["Uzbekistan", "USA", "Ukraine", "Palestine", "Egypt"])
        # widget.setEditable(True)
        # widget.setInsertPolicy(QComboBox.InsertAlphabetically)
        # widget.currentIndexChanged.connect(self.index_changed)
        # widget.currentTextChanged.connect(self.text_changed)
        # self.setCentralWidget(widget)


#     def index_changed(self, a):
#         print(f"Index o'zgardi: {a}")
#
#
#     def text_changed(self, a):
#         print(f"Text o'zgardi: {a}")
#
#
#     def c_checked(self, e):
#         self.b.setEnabled(e)
#
#
# window = MainWindow()
# window.show()
# app.exec()

# import pyqrcode
# a = pyqrcode.create("https://najottalim.uz/")
# a.png("qr.png", scale=10)








# import requests
# shahar = input()
# a = requests.get(f"https://islomapi.uz/api/present/week?region={shahar}")
# print(a.json())

from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QVBoxLayout, QHBoxLayout, QPushButton


class Color(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

class SecondWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        vl1 = QVBoxLayout()
        vl1.addWidget(Color("red"))
        vl1.addWidget(Color("green"))
        vl1.addWidget(Color("cyan"))
        w = QWidget()
        w.setLayout(vl1)
        self.setCentralWidget(w)


app = QApplication([])
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        vl1 = QVBoxLayout()
        vl1.addWidget(Color("red"))
        vl1.addWidget(Color("green"))
        vl1.addWidget(Color("cyan"))
        w = QWidget()
        w.setLayout(vl1)


        kh1 = QHBoxLayout()
        kh1.addWidget(Color("#af2798"))
        kh1.addWidget(Color("yellow"))
        kh1.addWidget(Color("#9900FF"))
        kh1.addWidget(Color("brown"))
        kw1 = QWidget()
        kw1.setLayout(kh1)

        kh2 = QHBoxLayout()
        kh2.addWidget(Color("magenta"))
        kh2.addWidget(Color("#000000"))
        kw2 = QWidget()
        kw2.setLayout(kh2)

        kh3 = QHBoxLayout()
        kh3.addWidget(Color("yellow"))
        kh3.addWidget(Color("blue"))
        kh3.addWidget(Color("cyan"))
        kw3 = QWidget()
        kw3.setLayout(kh3)
        vl2 = QVBoxLayout()
        vl2.addWidget(kw1)
        vl2.addWidget(kw2)
        vl2.addWidget(kw3)
        w2 = QWidget()
        w2.setLayout(vl2)
        c = QPushButton("Hello!")
        c.clicked.connect(self.click)
        ek = QHBoxLayout()
        ek.addWidget(w)
        ek.addWidget(w2)
        ek.addWidget(c)
        a = QWidget()
        a.setLayout(ek)
        self.setCentralWidget(a)

    def click(self):
        if self.a is None:
            self.a = SecondWindow()
            self.a.show()


q = MainWindow()
q.show()
app.exec()





# git
# VCS
# CLI
# cd
# repository
# repo
# clone
# add
# commit
# push
# pull











