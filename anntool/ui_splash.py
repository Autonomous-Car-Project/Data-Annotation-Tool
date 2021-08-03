from PySide6 import QtCore, QtGui, QtWidgets

class Ui_SplashScreen(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1075, 803)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 1055, 783))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 10, 1024, 768))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("assets/splash.png"))
        self.label.setObjectName("label")
        
        self.progressBar = QtWidgets.QProgressBar(self.frame)
        self.progressBar.setGeometry(QtCore.QRect(20, 614, 1024, 8))
        self.progressBar.setStyleSheet("QProgressBar {\n"
        "                    border: 0.1px solid grey;\n"
        "                    border-radius: 5px;\n"
        "                   background-color: rgba(255, 255, 255, 0);\n"
        "                   height: 200px;\n"
        "                \n"
        "               }\n"
        "               \n"
        "                QProgressBar::chunk {\n"
        "                    background-color: rgb(255, 255, 255);\n"
        "                    margin: 0;\n"
        "                   width: 3px;\n"
        "    \n"
        "                }")
        self.progressBar.setProperty("value", 30)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        
        self.ptext = QtWidgets.QLabel(self.frame)
        self.ptext.setGeometry(QtCore.QRect(30, 580, 131, 31))
        self.ptext.setStyleSheet("QLabel{\n"
        "    color: rgb(255,255,255);\n"
        "    \n"
        "    font: 18pt \"Reem Kufi\";\n"
        "}")
        self.ptext.setObjectName("ptext")
        
        self.info = QtWidgets.QLabel(self.frame)
        self.info.setGeometry(QtCore.QRect(850, 580, 191, 31))
        self.info.setStyleSheet("QLabel{\n"
        "    color: rgb(255,255,255);\n"
        "    \n"
        "    font: 18pt \"Reem Kufi\";\n"
        "}")
        self.info.setObjectName("info")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ptext.setText(_translate("MainWindow", "30 %"))
        self.info.setText(_translate("MainWindow", "Loading assets...."))
