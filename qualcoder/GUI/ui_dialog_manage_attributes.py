# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_dialog_manage_attributes.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_manage_attributes(object):
    def setupUi(self, Dialog_manage_attributes):
        Dialog_manage_attributes.setObjectName("Dialog_manage_attributes")
        Dialog_manage_attributes.resize(500, 500)
        self.gridLayout = QtWidgets.QGridLayout(Dialog_manage_attributes)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(Dialog_manage_attributes)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 36))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 36))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.pushButton_add = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_add.setGeometry(QtCore.QRect(30, 0, 32, 32))
        self.pushButton_add.setText("")
        self.pushButton_add.setObjectName("pushButton_add")
        self.pushButton_delete = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_delete.setGeometry(QtCore.QRect(120, 0, 32, 32))
        self.pushButton_delete.setText("")
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(190, 4, 281, 26))
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(Dialog_manage_attributes)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 1)

        self.retranslateUi(Dialog_manage_attributes)
        QtCore.QMetaObject.connectSlotsByName(Dialog_manage_attributes)

    def retranslateUi(self, Dialog_manage_attributes):
        _translate = QtCore.QCoreApplication.translate
        Dialog_manage_attributes.setWindowTitle(_translate("Dialog_manage_attributes", "Attributes"))
        self.pushButton_add.setToolTip(_translate("Dialog_manage_attributes", "<html><head/><body><p>Add</p></body></html>"))
        self.pushButton_delete.setToolTip(_translate("Dialog_manage_attributes", "<html><head/><body><p>Delete</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_manage_attributes = QtWidgets.QDialog()
    ui = Ui_Dialog_manage_attributes()
    ui.setupUi(Dialog_manage_attributes)
    Dialog_manage_attributes.show()
    sys.exit(app.exec_())
