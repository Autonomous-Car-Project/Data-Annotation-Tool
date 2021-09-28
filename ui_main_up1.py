
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QGraphicsDropShadowEffect, QApplication
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
from datetime import date
from datetime import datetime
from PyQt5.QtCore import QTimer, QTime, Qt
import glob

from src.mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.minimize_button.clicked.connect(self.minimize)
        self.ui.maximize_restore_button.clicked.connect(self.maximize)
        self.ui.close_button.clicked.connect(self.close_window)
        self.ui.imgPath_dropDown_button.clicked.connect(self.dialog_box)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000) # update every second
        self.state = 0
        self.date()
        self.showTime()


       
    def close_window(self):
        self.close()

    def minimize(self):
        self.showMinimized()
    
    def maximize(self):
        if self.state == 0:
            self.showMaximized()
            self.state = 1 
        else:
            self.showNormal()
            self.state = 0
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
        
        self.ui.date_label.setText(self.dat)   


    def showTime(self):
        self.currentTime = QTime.currentTime()

        self.displayTxt = self.currentTime.toString('hh:mm')
        

        self.ui.time_label.setText(self.displayTxt)
        
    def dialog_box(self):
            
        openfile =str(QFileDialog.getExistingDirectory(self, "Select a Folder"))
        print(openfile)
        a=glob.glob(openfile+"/*.*")
        print(a)

    

    
            
      
if __name__ == "__main__":
    import sys 
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
