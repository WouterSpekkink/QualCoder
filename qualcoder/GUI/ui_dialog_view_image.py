# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_dialog_view_image.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_view_image(object):
    def setupUi(self, Dialog_view_image):
        Dialog_view_image.setObjectName("Dialog_view_image")
        Dialog_view_image.resize(1021, 715)
        self.gridLayout = QtWidgets.QGridLayout(Dialog_view_image)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalSlider = QtWidgets.QSlider(Dialog_view_image)
        self.horizontalSlider.setMinimum(9)
        self.horizontalSlider.setSingleStep(3)
        self.horizontalSlider.setProperty("value", 99)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider.setTickInterval(10)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout.addWidget(self.horizontalSlider, 2, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(Dialog_view_image)
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 80))
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 3, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(Dialog_view_image)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1001, 583))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.graphicsView = QtWidgets.QGraphicsView(self.scrollAreaWidgetContents)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout_2.addWidget(self.graphicsView, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(Dialog_view_image)
        QtCore.QMetaObject.connectSlotsByName(Dialog_view_image)

    def retranslateUi(self, Dialog_view_image):
        _translate = QtCore.QCoreApplication.translate
        Dialog_view_image.setWindowTitle(_translate("Dialog_view_image", "View Image"))
        self.textEdit.setToolTip(_translate("Dialog_view_image", "<html><head/><body><p>Memo</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_view_image = QtWidgets.QDialog()
    ui = Ui_Dialog_view_image()
    ui.setupUi(Dialog_view_image)
    Dialog_view_image.show()
    sys.exit(app.exec_())
