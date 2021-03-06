from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 513)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        Dialog.setPalette(palette)
        self.userid_label = QtWidgets.QLabel(Dialog)
        self.userid_label.setGeometry(QtCore.QRect(73, 85, 60, 13))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.userid_label.setFont(font)
        self.userid_label.setObjectName("userid_label")
        self.username_label = QtWidgets.QLabel(Dialog)
        self.username_label.setGeometry(QtCore.QRect(74, 140, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.username_label.setFont(font)
        self.username_label.setObjectName("username_label")
        self.password_label = QtWidgets.QLabel(Dialog)
        self.password_label.setGeometry(QtCore.QRect(74, 201, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.password_label.setFont(font)
        self.password_label.setObjectName("password_label")
        self.email_label = QtWidgets.QLabel(Dialog)
        self.email_label.setGeometry(QtCore.QRect(75, 264, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.email_label.setFont(font)
        self.email_label.setObjectName("email_label")
        self.branch_label = QtWidgets.QLabel(Dialog)
        self.branch_label.setGeometry(QtCore.QRect(74, 335, 60, 13))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.branch_label.setFont(font)
        self.branch_label.setObjectName("branch_label")
        self.gender_label = QtWidgets.QLabel(Dialog)
        self.gender_label.setGeometry(QtCore.QRect(73, 394, 60, 13))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.gender_label.setFont(font)
        self.gender_label.setObjectName("gender_label")
        self.userid_entry = QtWidgets.QLineEdit(Dialog)
        self.userid_entry.setGeometry(QtCore.QRect(216, 76, 190, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.userid_entry.setFont(font)
        self.userid_entry.setMaxLength(15)
        self.userid_entry.setObjectName("userid_entry")
        self.username_entry = QtWidgets.QLineEdit(Dialog)
        self.username_entry.setGeometry(QtCore.QRect(216, 134, 190, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.username_entry.setFont(font)
        self.username_entry.setMaxLength(50)
        self.username_entry.setObjectName("username_entry")
        self.password_entry = QtWidgets.QLineEdit(Dialog)
        self.password_entry.setGeometry(QtCore.QRect(216, 194, 190, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.password_entry.setFont(font)
        self.password_entry.setWhatsThis("")
        self.password_entry.setMaxLength(20)
        self.password_entry.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.password_entry.setObjectName("password_entry")
        self.email_entry = QtWidgets.QLineEdit(Dialog)
        self.email_entry.setGeometry(QtCore.QRect(217, 256, 190, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.email_entry.setFont(font)
        self.email_entry.setMaxLength(50)
        self.email_entry.setObjectName("email_entry")
        self.branch_entry = QtWidgets.QComboBox(Dialog)
        self.branch_entry.setGeometry(QtCore.QRect(218, 325, 190, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.branch_entry.setFont(font)
        self.branch_entry.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.branch_entry.setObjectName("branch_entry")
        self.branch_entry.addItem("")
        self.branch_entry.addItem("")
        self.branch_entry.addItem("")
        self.branch_entry.addItem("")
        self.branch_entry.addItem("")
        self.gender_entry1 = QtWidgets.QRadioButton(Dialog)
        self.gender_entry1.setGeometry(QtCore.QRect(227, 393, 51, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.gender_entry1.setFont(font)
        self.gender_entry1.setObjectName("gender_entry1")
        self.gender_entry2 = QtWidgets.QRadioButton(Dialog)
        self.gender_entry2.setGeometry(QtCore.QRect(319, 393, 81, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.gender_entry2.setFont(font)
        self.gender_entry2.setObjectName("gender_entry2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(190, 460, 100, 26))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.pushButton.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.title = QtWidgets.QLabel(Dialog)
        self.title.setGeometry(QtCore.QRect(132, 20, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.title.setFont(font)
        self.title.setTextFormat(QtCore.Qt.PlainText)
        self.title.setObjectName("title")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Registration Form"))
        self.userid_label.setText(_translate("Dialog", "UserID"))
        self.username_label.setText(_translate("Dialog", "Username"))
        self.password_label.setText(_translate("Dialog", "Password"))
        self.email_label.setText(_translate("Dialog", "Email"))
        self.branch_label.setText(_translate("Dialog", "Branch"))
        self.gender_label.setText(_translate("Dialog", "Gender"))
        self.branch_entry.setItemText(0, _translate("Dialog", "IT"))
        self.branch_entry.setItemText(1, _translate("Dialog", "ME"))
        self.branch_entry.setItemText(2, _translate("Dialog", "EEE"))
        self.branch_entry.setItemText(3, _translate("Dialog", "CSE"))
        self.branch_entry.setItemText(4, _translate("Dialog", "ECE"))
        self.gender_entry1.setText(_translate("Dialog", "Male"))
        self.gender_entry2.setText(_translate("Dialog", "Female"))
        self.pushButton.setText(_translate("Dialog", "Submit"))
        self.title.setText(_translate("Dialog", "PLEASE  FILL  UP  THE  DETAILS"))
