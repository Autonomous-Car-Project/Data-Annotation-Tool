from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QGraphicsDropShadowEffect, QApplication

from src.mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.minimize_button.clicked.connect(self.minimize)
        self.ui.maximize_restore_button.clicked.connect(self.maximize)
        self.ui.close_button.clicked.connect(self.close_window)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.state = 0

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

if __name__ == "__main__":
    import sys 
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())