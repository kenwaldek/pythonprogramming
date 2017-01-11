#! /usr/bin/env python3
#  -*- coding:utf-8 -*-
###############################################################
# kenwaldek                           GPL-license

# Title: PyQt5 lesson 4               Version: 1.0
# Date: 08-01-17                      Language: python3
# Description: pyqt5 gui and button function
# pythonprogramming.net from PyQt4 to PyQt5
###############################################################

# do something
import sys
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton


class window(QMainWindow):

    def __init__(self):
        super(window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle('pyqt5 Tut')
        # self.setWindowIcon(QIcon('pic.png'))
        self.home()

    def home(self):
        btn = QPushButton('quit', self)
        btn.clicked.connect(self.close_application)

        btn.resize(btn.sizeHint())  #set to acceptable size automatic
        btn.move(0, 0)
        self.show()

    def close_application(self):
        print('whooo so custom')
        sys.exit()

def run():
    app = QApplication(sys.argv)
    Gui = window()
    sys.exit(app.exec_())

run()
