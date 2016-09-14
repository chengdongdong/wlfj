#!/usr/bin/python

# menubar.py

import sys
from PyQt4 import QtGui, QtCore

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.setWindowTitle('logistics')
        self.showMaximized()

        about = QtGui.QAction(QtGui.QIcon('about.png'), 'About', self)
        about.setShortcut('Ctrl+B')
        about.setStatusTip('About application')
        self.connect(about, QtCore.SIGNAL('triggered()'), self.about_dialog)

        exit = QtGui.QAction(QtGui.QIcon('exit.png'), 'Exit', self)
        exit.setShortcut('Ctrl+Q')
        exit.setStatusTip('Exit application')
        self.connect(exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))

        self.statusBar()

        menubar = self.menuBar()
        file = menubar.addMenu('&File')
        file.addAction(about)
        file.addAction(exit)

    def about_dialog(self):
        self.statusBar().showMessage('About')

app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())
