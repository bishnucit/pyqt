# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewUser_Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Register_Dialog(object):
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
        self.cancel_btn = QtWidgets.QPushButton(self.groupBox)
        self.add_btn.clicked.connect(self.Add_btn)
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


