#! /usr/bin/env python3
#  -*- coding:utf-8 -*-
###############################################################
# kenwaldek                           GPL-license

# Title: PyQt5 lesson 2               Version: 1.0
# Date: 08-01-17                      Language: python3
# Description: pyqt5 gui empty window with title
# pythonprogramming.net from PyQt4 to PyQt5
###############################################################

# do something
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

class window(QMainWindow):

    def __init__(self):
        super(window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle('pyqt5 Tut')
        # self.setWindowIcon(QIcon('pic.png'))
        self.show()

app = QApplication(sys.argv)
Gui = window()
sys.exit(app.exec_())
