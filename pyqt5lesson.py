# GUI => Graphical User Interface
# UI/UX
# User interface, User Experience
# TZ

# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, \
#     QMainWindow, QLineEdit, QVBoxLayout, QLabel, QMenu, QAction
#
# app = QApplication([])

# window = QWidget()
# window.show()  # IMPORTANT!!!!! Windows are hidden by default.
# a = QPushButton("Hello Buddy")
# a.show()

# w = QMainWindow()
# w.show()


# class Orifjon(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("Najot Ta'lim")
#         # b = QInputDialog()
#         self.setMaximumSize(900, 800)
#         self.setCentralWidget(b)
#
#
#
# a = Orifjon()
# a.show()

# Start the event loop.
# app.exec()


# Your application won't reach here until you exit and the event
# loop has stopped.




# class MainWindow(QMainWindow):
#
#     def __init__(self):
#         super().__init__()
#         self.n = 0
#         self.setWindowTitle("Najot Ta'lim")
#         self.b = QPushButton("Click!")
#         self.b.setCheckable(True)
#         # b.clicked.connect(self.salom)
#         self.clicked.connect(self.xayr)
#         self.setCentralWidget(self.b)
#
#
#     def salom(self, a):
#         self.n += 10
#         if a:
#             print("Men Bosildim!!!!!")
#         else:
#             print("Qayttim!!!")
#         self.setWindowTitle(f"{self.n}")
#
#     def xayr(self):
#         self.b.setEnabled(False)
#         self.b.setText("Men Bosildim, uzr...")


#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#
#
#     def contextMenuEvent(self, e):
#         context = QMenu(self)
#         context.addAction(QAction("New Folder", self))
#         context.addAction(QAction("Get Info", self))
#         context.addAction(QAction("CHange Bakcground", self))
#         context.exec(e.globalPos())
#



        # self.label = QLabel("Meni Bos!!!")
        # self.label.setLineWidth(4)
        # self.label.setMaximumSize(300, 300)
        # self.setCentralWidget(self.label)
        # self.label.setMargin(100)

    #
    # def mouseMoveEvent(self, e):
    #     self.label.setText("mouseMoveEventmouseMoveEvent")
    #
    # def mousePressEvent(self, e):
    #     self.label.setText("mousePressEvent")
    #
    # def mouseReleaseEvent(self, e):
    #     self.label.setText("mouseReleaseEvent")
    #
    # def mouseDoubleClickEvent(self, e):
    #     self.label.setText("mouseDoubleClickEvent")


        # self.input = QLineEdit()
        #
        # self.input.textChanged.connect(self.label.setText)
        #
        # layout = QVBoxLayout()
        # layout.addWidget(self.input)
        # layout.addWidget(self.label)
        #
        # container = QWidget()
        # container.setLayout(layout)
        #
        # # Set the central widget of the Window.
        # self.setCentralWidget(container)





# window = MainWindow()
# window.show()
#
# app.exec()
import sys

from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
    QTextEdit
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMaximumSize(600, 600)
        self.setWindowTitle("My Window!!")
        self.a = QTextEdit()
        # self.a = QLabel("Hello")
        # self.a.setMaximumSize(600, 600)
        # self.a.setScaledContents(True)
        # font = self.a.font()
        # font.setPointSize(16)
        # self.a.setFont(font)
        # self.setCentralWidget(self.a)
        # self.a.setAlignment(Qt.AlignVCenter | Qt.AlignJustify)
        # self.a.setPixmap(QPixmap('yorichi1.png'))



        # self.setWindowTitle("Widgets App")
        # layout = QVBoxLayout()



        widgets = [
            QCheckBox,
            QComboBox,
            QDateEdit,
            QDateTimeEdit,
            QDial,
            QDoubleSpinBox,
            QFontComboBox,
            QLCDNumber,
            QLabel,
            QLineEdit,
            QProgressBar,
            QPushButton,
            QRadioButton,
            QSlider,
            QSpinBox,
            QTimeEdit,
        ]

        # layout.addWidget(QSpinBox())
        # layout.addWidget(QSlider())

        # for w in widgets:
        #     layout.addWidget(w())

        # widget = QWidget()
        # widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        # self.setCentralWidget(widget)





app = QApplication([])
window = MainWindow()
window.show()
app.exec()
