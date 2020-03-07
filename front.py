from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from login import LoginMainClass
from register import RegisterMainClass

class FrontMainClass(object):
    def setupUi(self, frontDialog):
        frontDialog.setObjectName("frontDialog")
        frontDialog.resize(394, 339)
        self.label = QtWidgets.QLabel(frontDialog)
        self.label.setGeometry(QtCore.QRect(88, 40, 225, 41))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 127);")
        self.label.setObjectName("label")
        self.im2 = QPixmap("./f-login.png")
        self.label_2 = QtWidgets.QLabel(frontDialog)
        self.label_2.setGeometry(QtCore.QRect(25, 89, 111, 101))
        self.label_2.setObjectName("label_2")
        self.label_2.setPixmap(self.im2)
        self.im3 = QPixmap("./f-user-add.png")
        self.label_3 = QtWidgets.QLabel(frontDialog)
        self.label_3.setGeometry(QtCore.QRect(25, 214, 111, 101))
        self.label_3.setObjectName("label_3")
        self.label_3.setPixmap(self.im3)
        self.label_4 = QtWidgets.QLabel(frontDialog)
        self.label_4.setGeometry(QtCore.QRect(152, 10, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(17)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 0, 127);")
        self.label_4.setObjectName("label_4")


        self.LOGIN = QtWidgets.QPushButton(frontDialog)
        self.LOGIN.setGeometry(QtCore.QRect(200, 110, 140, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.LOGIN.setFont(font)
        self.LOGIN.setStyleSheet("background-color: rgb(82, 22, 20);\n"
        "color: rgb(255, 255, 255);")
        self.LOGIN.setObjectName("LOGIN")
        self.LOGIN.clicked.connect(self.loginDialogOpen)

        
        self.REGISTER = QtWidgets.QPushButton(frontDialog)
        self.REGISTER.setGeometry(QtCore.QRect(200, 235, 140, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.REGISTER.setFont(font)
        self.REGISTER.setStyleSheet("background-color: rgb(82, 22, 20);\n"
        "color: rgb(255, 255, 255);")
        self.REGISTER.setObjectName("REGISTER")
        self.REGISTER.clicked.connect(self.registerDialogOpen)


        self.retranslateUi(frontDialog)
        QtCore.QMetaObject.connectSlotsByName(frontDialog)

    def retranslateUi(self, frontDialog):
        _translate = QtCore.QCoreApplication.translate
        frontDialog.setWindowTitle(_translate("Dialog", "Select your choice"))
        self.label.setText(_translate("Dialog", "Select Your Choice"))
        self.label_4.setText(_translate("Dialog", "WELCOME"))
        self.LOGIN.setText(_translate("Dialog", "LOGIN"))
        self.REGISTER.setText(_translate("Dialog", "REGISTER"))

    def loginDialogOpen(self):
        self.dialog = QtWidgets.QDialog()
        self.ui = LoginMainClass()
        self.ui.setupUi(self.dialog)
        frontDialog.hide()
        self.dialog.show()

    def registerDialogOpen(self):
        self.dialog = QtWidgets.QDialog()
        self.ui = RegisterMainClass()
        self.ui.setupUi(self.dialog)
        frontDialog.hide()
        self.dialog.show()


if __name__ == "__main__":  
    import sys  
    app = QtWidgets.QApplication(sys.argv)  
    frontDialog = QtWidgets.QDialog()  
    ui = FrontMainClass()  
    ui.setupUi(frontDialog)  
    frontDialog.show()  
    sys.exit(app.exec_())


