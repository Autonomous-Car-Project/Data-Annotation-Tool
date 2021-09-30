from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication

from src.mainwindow import Ui_MainWindow

Global_state = 0

class UI_Functions(Ui_MainWindow):
 
    def close_window(self):
        self.close()

    def minimize(self):
        self.showMinimized()
    
    def maximize(self):
        global Global_state
        status = Global_state
        if status == 0:
            Global_state = 1
            self.showMaximized() 
        else:
            Global_state = 0
            self.showNormal()
            

    def UI_Definition(self):
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.ui.close_button.clicked.connect(lambda: UI_Functions.close_window(self))
        self.ui.maximize_restore_button.clicked.connect(lambda: UI_Functions.maximize(self))
        self.ui.minimize_button.clicked.connect(lambda: UI_Functions.minimize(self))