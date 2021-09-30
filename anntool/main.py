import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QMainWindow, QGraphicsDropShadowEffect, QApplication
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
from datetime import date
from datetime import datetime
from PyQt5.QtCore import QTimer, QTime, Qt
import glob
from ui_splash import Ui_SplashScreen

from src.mainwindow import Ui_MainWindow

from src.utils.minmaxclose import *

counter=0

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #QtCore.QTimer.singleShot(1500, lambda: self.ui.date_label.setText("<strong>Successful</strong>"))
        #QtCore.QTimer.singleShot(1500, lambda: self.setStyleSheet("background-color: #222; color: #FFF"))

        UI_Functions.UI_Definition(self)

        self.ui.imgPath_dropDown_button.clicked.connect(self.dialog_box)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000) # update every second
        self.state = 0
        self.date()
        self.showTime()

    def date(self):
        
        now = datetime.now()
        self.dat=now.strftime("%d %B,%Y")
      
        if(self.dat[1]=='1' and self.dat[0]!='1'):
            self.dat=now.strftime("%dst %B,%Y")
        elif(self.dat[1]=='2' and self.dat[0]!='1'):
            self.dat=now.strftime("%dnd %B,%Y")
        elif(self.dat[1]=='3' and self.dat[0]!='1'):
            self.dat=now.strftime("%drd %B,%Y") 
        else:
            self.dat=now.strftime("%dth %B,%Y")                   
        _translate = QtCore.QCoreApplication.translate
        self.ui.date_label.setText(_translate(" ", self.dat))   


    def showTime(self):
        self.currentTime = QTime.currentTime()

        self.displayTxt = self.currentTime.toString('hh:mm')
        

        self.ui.time_label.setText(self.displayTxt)
        
    def dialog_box(self):
            
        openfile =str(QFileDialog.getExistingDirectory(self, "Select a Folder"))
        print(openfile)
        a=glob.glob(openfile+"/*.*")
        print(a)

class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))

        self.ui.frame.setGraphicsEffect(self.shadow)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(35)

        self.ui.info.setText("Getting Started ....")

        QtCore.QTimer.singleShot(1500, lambda: self.ui.info.setText("Loading assets ..."))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.info.setText("Starting ..."))

        self.show()

    def progress(self):
        global counter
        self.ui.progressBar.setValue(counter)
        self.ui.ptext.setText(f"{counter} %")
        if counter > 100:
            self.timer.stop()
            self.main = MainWindow()
            self.main.show()
            self.close()
        counter += 1




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec())