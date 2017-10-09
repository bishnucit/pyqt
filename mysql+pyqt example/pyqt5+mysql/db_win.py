# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DB_window.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import DB_manager,sys

class Ui_TPayne_MySQL_Tool(QtWidgets.QWidget):
    def __init__(self, database, tableName):
        QtWidgets.QWidget.__init__(self)
        self.dbu = DB_manager.DatabaseUtility(database, tableName)
        self.setupUi(self)
        self.UpdateTree()

    def setupUi(self, TPayne_MySQL_Tool):
        TPayne_MySQL_Tool.setObjectName("TPayne_MySQL_Tool")
        TPayne_MySQL_Tool.resize(457, 235)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(TPayne_MySQL_Tool)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(TPayne_MySQL_Tool)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(TPayne_MySQL_Tool)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.commitButton = QtWidgets.QPushButton(TPayne_MySQL_Tool)
        self.commitButton.setObjectName("commitButton")
        self.commitButton.clicked.connect(self.Commit)

        self.horizontalLayout.addWidget(self.commitButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.treeWidget = QtWidgets.QTreeWidget(TPayne_MySQL_Tool)
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.verticalLayout.addWidget(self.treeWidget)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(TPayne_MySQL_Tool)
        QtCore.QMetaObject.connectSlotsByName(TPayne_MySQL_Tool)

    def retranslateUi(self, TPayne_MySQL_Tool):
        _translate = QtCore.QCoreApplication.translate
        TPayne_MySQL_Tool.setWindowTitle(_translate("TPayne_MySQL_Tool", "TPayne\'s MySQL Message Storer"))
        self.label.setText(_translate("TPayne_MySQL_Tool", "Super Fancy Title!"))
        self.lineEdit.setText(_translate("TPayne_MySQL_Tool", "steak"))
        self.commitButton.setText(_translate("TPayne_MySQL_Tool", "Commit!"))
        self.treeWidget.headerItem().setText(0, _translate("TPayne_MySQL_Tool", "1"))
        self.treeWidget.headerItem().setText(1, _translate("TPayne_MySQL_Tool", "New Column"))
        self.treeWidget.headerItem().setText(2, _translate("TPayne_MySQL_Tool", "2"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("TPayne_MySQL_Tool", "test2"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("TPayne_MySQL_Tool", "test233"))
        self.treeWidget.topLevelItem(1).setText(1, _translate("TPayne_MySQL_Tool", "asdf"))
        self.treeWidget.topLevelItem(1).setText(2, _translate("TPayne_MySQL_Tool", "asdf"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)


    def Commit(self):
        print("---------------------------------------------")
        text = self.lineEdit.text()

        print(text)
        self.dbu.AddEntryToTable(text)
        self.UpdateTree()

    def UpdateTree(self):
        col = self.dbu.GetColumns()
        table = self.dbu.GetTable()

        for c in range(len(col)):
            self.treeWidget.headerItem().setText(c, col[c][0])

        self.treeWidget.clear()

        print(table)

        for item in range(len(table)):
            QtWidgets.QTreeWidgetItem(self.treeWidget)
            for value in range(len(table[item])):
                self.treeWidget.topLevelItem(item).setText(value, str(table[item][value]))



if __name__ == "__main__":
    import sys
    db='first'
    tableName='first'
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_TPayne_MySQL_Tool(db, tableName)
    ex.show()
    x = app.exec_()

    sys.exit(x)
