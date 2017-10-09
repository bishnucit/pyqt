
#!/usr/bin/env python

import sys
import DB_manager as db
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login_Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.dbu = db.DatabaseUtility('UsernamePassword_DB', 'masterTable')
        self.setupUi(self)
        self.confirm = None

    def setupUi(self, Login_Dialog):
        Login_Dialog.setObjectName("Login_Dialog")
        Login_Dialog.resize(285, 134)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Login_Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Login_Dialog)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.user_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.user_lineEdit.setObjectName("user_lineEdit")
        self.horizontalLayout.addWidget(self.user_lineEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.password_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.password_lineEdit.setInputMask("")
        self.password_lineEdit.setText("")
        self.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.horizontalLayout_2.addWidget(self.password_lineEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.newUser_btn = QtWidgets.QPushButton(self.groupBox)
        self.newUser_btn.setObjectName("newUser_btn")
        self.horizontalLayout_4.addWidget(self.newUser_btn)
        self.newUser_btn.clicked.connect(self.NewUser_btn)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.login_btn = QtWidgets.QPushButton(self.groupBox)
        self.login_btn.setObjectName("login_btn")
        self.horizontalLayout_4.addWidget(self.login_btn)
        self.login_btn.clicked.connect(self.Login_btn)

        self.cancel_btn = QtWidgets.QPushButton(self.groupBox)
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout_4.addWidget(self.cancel_btn)
        self.cancel_btn.clicked.connect(self.Cancel_btn)

        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addWidget(self.groupBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Login_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Login_Dialog)

    def retranslateUi(self, Login_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Login_Dialog.setWindowTitle(_translate("Login_Dialog", "TPayne\'s User Login"))
        self.groupBox.setTitle(_translate("Login_Dialog", "Super Ham!"))
        self.label.setText(_translate("Login_Dialog", "Username"))
        self.label_2.setText(_translate("Login_Dialog", "Password"))
        self.newUser_btn.setText(_translate("Login_Dialog", "New User"))
        self.login_btn.setText(_translate("Login_Dialog", "Login"))
        self.cancel_btn.setText(_translate("Login_Dialog", "Cancel"))


    #@QtCore.pyqtSignature("on_cancel_btn_clicked()")
    def Cancel_btn(self):
        self.close()

    #@QtCore.pyqtSignature("on_login_btn_clicked()")
    def Login_btn(self):
        username = self.user_lineEdit.text()
        password = self.password_lineEdit.text()
        if not username:
            QtWidgets.QMessageBox.warning(self, 'Guess What?', 'Username Missing!')
        elif not password:
            QtWidgets.QMessageBox.warning(self, 'Guess What?', 'Password Missing!')
        else:
            self.AttemptLogin(username, password)

    def AttemptLogin(self, username, password):
        t = self.dbu.GetTable()
        print (t)
        for col in t:
            if username == col[1]:
                if password == col[2]:
                    QtWidgets.QMessageBox.information(self, 'BOOYA!', 'Success!!')
                    self.close()
                else:
                    QtWidgets.QMessageBox.warning(self, 'Dang it!', 'Password incorrect...')
                    return

    #@QtCore.pyqtSignature("on_newUser_btn_clicked()")
    def NewUser_btn(self):
        self.newUser = Ui_Register(self.dbu)
        self.newUser.show()

class Ui_Register(QtWidgets.QDialog):
    def __init__(self, dbu):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        self.dbu = dbu

    def setupUi(self, Register_Dialog):
        Register_Dialog.setObjectName("Register_Dialog")
        Register_Dialog.resize(372, 187)
        Register_Dialog.setModal(True)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Register_Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Register_Dialog)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.username_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.username_lineEdit.setObjectName("username_lineEdit")
        self.horizontalLayout.addWidget(self.username_lineEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.password_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.horizontalLayout_2.addWidget(self.password_lineEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.confirmPassword_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.confirmPassword_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmPassword_lineEdit.setObjectName("confirmPassword_lineEdit")
        self.horizontalLayout_4.addWidget(self.confirmPassword_lineEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.add_btn = QtWidgets.QPushButton(self.groupBox)
        self.add_btn.setObjectName("add_btn")
        self.horizontalLayout_3.addWidget(self.add_btn)
        self.add_btn.clicked.connect(self.Add_btn)

        self.cancel_btn = QtWidgets.QPushButton(self.groupBox)
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout_3.addWidget(self.cancel_btn)
        self.cancel_btn.clicked.connect(self.Cancel_btn)

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addWidget(self.groupBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Register_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Register_Dialog)

    def retranslateUi(self, Register_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Register_Dialog.setWindowTitle(_translate("Register_Dialog", "Register New User"))
        self.groupBox.setTitle(_translate("Register_Dialog", "I Love Ham!"))
        self.label_2.setText(_translate("Register_Dialog", "Username"))
        self.label.setText(_translate("Register_Dialog", "Password"))
        self.label_3.setText(_translate("Register_Dialog", "Confirm Password"))
        self.label_4.setText(_translate("Register_Dialog", "Not Included: Phone, Address, Social Security Number, Credit Card..."))
        self.add_btn.setText(_translate("Register_Dialog", "Add"))
        self.cancel_btn.setText(_translate("Register_Dialog", "Cancel"))


    #@QtCore.pyqtSignature("on_cancel_btn_clicked()")
    def Cancel_btn(self):
        self.close()

    #@QtCore.pyqtSignature("on_add_btn_clicked()")
    def Add_btn(self):
        username = self.username_lineEdit.text()
        password = self.password_lineEdit.text()
        cpassword = self.confirmPassword_lineEdit.text()
        if not username:
            QtWidgets.QMessageBox.warning(self, 'Dang it!', 'Username Missing')
        elif password != cpassword:
            QtWidgets.QMessageBox.warning(self, 'Dang it!', 'Passwords Do Not Match')
        else:
            t = self.dbu.GetTable()
            print (t)
            for col in t:
                if username == col[1]:
                    QtWidgets.QMessageBox.warning(self, 'Dang it!', 'Username Taken. :(')
            else:
                self.dbu.AddEntryToTable (username, password)
                QtWidgets.QMessageBox.information(self, 'Awesome!!', 'User Added SUCCESSFULLY!')
                self.close()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_Login()
    ex.show()
    sys.exit(app.exec_())
