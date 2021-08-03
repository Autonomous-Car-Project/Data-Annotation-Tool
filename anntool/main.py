import sys
from PySide6 import QtCore
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QMainWindow, QGraphicsDropShadowEffect, QApplication

from ui_splash import Ui_SplashScreen

from ui_main import Ui_MainWindow

counter = 0

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        QtCore.QTimer.singleShot(1500, lambda: self.ui.label.setText("<strong>Successful</strong>"))
        QtCore.QTimer.singleShot(1500, lambda: self.setStyleSheet("background-color: #222; color: #FFF"))


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