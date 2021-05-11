# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import requests
import mysql.connector as mc
from signup import SignUp

class Login(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 249)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 401, 71))
        self.frame.setStyleSheet("background-color: green;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 0, 401, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 51, 21))
        self.label_2.setObjectName("label_2")
        self.usernameEdit = QtWidgets.QLineEdit(Form)
        self.usernameEdit.setGeometry(QtCore.QRect(70, 90, 301, 21))
        self.usernameEdit.setObjectName("usernameEdit")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(10, 120, 51, 21))
        self.label_5.setObjectName("label_5")
        self.passwordEdit = QtWidgets.QLineEdit(Form)
        self.passwordEdit.setGeometry(QtCore.QRect(70, 120, 301, 21))
        self.passwordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordEdit.setObjectName("passwordEdit")

        self.loginButton = QtWidgets.QPushButton(Form)
        self.loginButton.setGeometry(QtCore.QRect(260, 180, 111, 51))
        self.loginButton.setObjectName("loginButton")
        self.loginButton.clicked.connect(self.login)

        self.signupButton = QtWidgets.QPushButton(Form)
        self.signupButton.setGeometry(QtCore.QRect(140, 180, 111, 51))
        self.signupButton.setObjectName("signupButton")
        self.signupButton.clicked.connect(self.openSignUp)

        self.login_result = QtWidgets.QLabel(Form)
        self.login_result.setGeometry(QtCore.QRect(10, 180, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.login_result.setFont(font)
        self.login_result.setStyleSheet("color: red")
        self.login_result.setText("")
        self.login_result.setAlignment(QtCore.Qt.AlignCenter)
        self.login_result.setObjectName("login_result")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Login"))
        self.label_2.setText(_translate("Form", "Username:"))
        self.label_5.setText(_translate("Form", "Password:"))
        self.loginButton.setText(_translate("Form", "Login"))
        self.signupButton.setText(_translate("Form", "Create Account"))

    def login(self):
        url="http://localhost:8080/api/auth/signin"
        username = self.usernameEdit.text()
        password = self.passwordEdit.text()

        response = requests.post(url, data={"username": username, "password": password})

        result = response.status_code
        print(result)
        print(response.json())


    def openSignUp(self):
        self.Form = QtWidgets.QWidget()
        self.ui = SignUp()
        self.ui.setupUi(self.Form)
        self.Form.show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    Form = QtWidgets.QWidget()
    ui = Login()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
