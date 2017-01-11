#! /usr/bin/env python3
#  -*- coding:utf-8 -*-
###############################################################
# kenwaldek                           GPL-license

# Title: PyQt5 lesson 6               Version: 1.0
# Date: 08-01-17                      Language: python3
# Description: pyqt5 gui add toolbar
# pythonprogramming.net from PyQt4 to PyQt5
###############################################################

# do something
import sys
from PyQt5.QtCore import QCoreApplication
# from PyQt5.QtGui import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QAction
from PyQt5.uic.properties import QtGui


class window(QMainWindow):

    def __init__(self):
        super(window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle('pyqt5 Tut')
        # self.setWindowIcon(QIcon('pic.png'))

        extractAction = QAction('&Get to the choppah', self)
        extractAction.setShortcut('Ctrl+Q')
        extractAction.setStatusTip('leave the app')
        extractAction.triggered.connect(self.close_application)

        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)

        extractAction = QAction(QIcon('pic.png'), 'flee the scene', self)
        extractAction.triggered.connect(self.close_application)

        self.toolBar = self.addToolBar('Extraction')
        self.toolBar.addAction(extractAction)

        self.home()

    def home(self):
        btn = QPushButton('quit', self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.sizeHint())
        btn.move(0, 100)

        self.show()

    def close_application(self):
        print('whooo so custom')
        sys.exit()

if __name__ == "__main__":
    def run():
        app = QApplication(sys.argv)
        Gui = window()
        sys.exit(app.exec_())

run()
