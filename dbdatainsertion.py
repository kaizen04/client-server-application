from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSlot
import mysql.connector as mdb
from register import RegisterMainClass

class RegisterValues(QMainWindow, RegisterMainClass):
    def __init__(self):
        super(RegisterValues, self).__init__()
        self.setupUi(self)
        self.pushButton.setEnabled(False)

    def initWindow(self):
        self.userid_entry.textChanged.connect(self.newText)
        self.username_entry.textChanged.connect(self.newText)
        self.password_entry.textChanged.connect(self.newText)
        self.email_entry.textChanged.connect(self.newText)
        self.branch_entry.textChanged.connect(self.newText)
        self.gender_entry1.textChanged.connect(self.newText)
        self.gender_entry2.textChanged.connect(self.newText)

        self.pushButton.clicked.connect(self.InsertData)

    @pyqtSlot()
    def insertData(self):
        con = mdb.connect(host="localhost",user="root", passwd="1234",db="registration")

        with con:
            cur = con.cursor()  
            cur.execute('''INSERT INTO students(userid, username, password, email, branch, gender)
                           VALUES (%d, %s, %s, %s, %s, %s)''', 
                           ( self.userid_entry.text(),
                             self.username_entry.text(),
                             self.password_entry.text(),
                             self.email_entry.text(),
                             self.branch_entry.itemText(),
                             self.gender_entry1.text(),
                             self.gender_entry2.text() )
                       )            
            cur.close()

            QMessageBox.information(self, "Connection", "Data Inserted Successfully")

            self.userid_entry.setText('')
            self.username_entry.setText('')
            self.password_entry.setText('')
            self.email_entry.setText('')
            self.branch_entry.setItemText('')
            self.gender_entry1.setText(False)
            self.gender_entry2.setText(False) 

    def newText(self):
        if self.userid_entry.text() and self.username_entry.text() and self.password_entry.text() and self.email_entry.text() and self.branch_entry.text() and (self.gender_entry1.text() or self.gender_entry2.text()):
            self.button.setEnabled(True)
        else:
            self.button.setEnabled(False)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = RegisterValues()
    MainWindow.show()
    sys.exit(app.exec_())




