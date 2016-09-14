#!/usr/bin/python

# menubar.py

import sys
from PyQt4 import QtGui, QtCore

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.setWindowTitle('logistics')
        self.showMaximized()

        #self.ui_bar_search()
        self.hbox1 = QtGui.QHBoxLayout()
        self.hbox1.addStretch(1)
        #hbox1.addWidget(okButton)
        #hbox1.addWidget(cancelButton)

        self.vbox1 = QtGui.QVBoxLayout()
        #vbox.addStretch(1)

        #about = QtGui.QAction(QtGui.QIcon('about.png'), 'About', self)
        #about.setShortcut('Ctrl+B')
        #about.setStatusTip('About application')
        #self.connect(about, QtCore.SIGNAL('triggered()'), self.about_dialog)

        #exit = QtGui.QAction(QtGui.QIcon('exit.png'), 'Exit', self)
        #exit.setShortcut('Ctrl+Q')
        #exit.setStatusTip('Exit application')
        #self.connect(exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))

        #self.vbox1.addWidget(self.searchEdit)
        
        self.textEdit = QtGui.QTextEdit()
        #self.setCentralWidget(self.textEdit)
        self.hbox1.addWidget(self.textEdit)
        self.hbox1.addStretch(1)
        #self.statusBar()
        self.vbox1.addLayout(self.hbox1)
        self.setLayout(self.vbox1)

        #menubar = self.menuBar()
        #file = menubar.addMenu('&File')
        #file.addAction(about)
        #file.addAction(exit)

    def ui_bar_search(self):
        title = QtGui.QLabel('Title')
        author = QtGui.QLabel('Author')
        review = QtGui.QLabel('Review')

        titleEdit = QtGui.QLineEdit()
        authorEdit = QtGui.QLineEdit()
        reviewEdit = QtGui.QTextEdit()

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)

        self.setLayout(grid)


    #def about_dialog(self):
        #self.statusBar().showMessage('About')

app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())
