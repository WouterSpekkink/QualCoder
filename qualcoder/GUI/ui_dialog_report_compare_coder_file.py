# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_dialog_report_compare_coder_file.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_reportCompareCoderFile(object):
    def setupUi(self, Dialog_reportCompareCoderFile):
        Dialog_reportCompareCoderFile.setObjectName("Dialog_reportCompareCoderFile")
        Dialog_reportCompareCoderFile.setWindowModality(QtCore.Qt.NonModal)
        Dialog_reportCompareCoderFile.resize(989, 580)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog_reportCompareCoderFile)
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Dialog_reportCompareCoderFile)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 120))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 120))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 101, 22))
        self.label_2.setObjectName("label_2")
        self.comboBox_coders = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_coders.setGeometry(QtCore.QRect(112, 20, 211, 28))
        self.comboBox_coders.setObjectName("comboBox_coders")
        self.label_exports = QtWidgets.QLabel(self.groupBox)
        self.label_exports.setGeometry(QtCore.QRect(300, 84, 24, 24))
        self.label_exports.setText("")
        self.label_exports.setObjectName("label_exports")
        self.label_title = QtWidgets.QLabel(self.groupBox)
        self.label_title.setGeometry(QtCore.QRect(10, -2, 291, 22))
        self.label_title.setObjectName("label_title")
        self.label_matrix = QtWidgets.QLabel(self.groupBox)
        self.label_matrix.setGeometry(QtCore.QRect(600, 20, 30, 30))
        self.label_matrix.setText("")
        self.label_matrix.setObjectName("label_matrix")
        self.label_memos = QtWidgets.QLabel(self.groupBox)
        self.label_memos.setGeometry(QtCore.QRect(600, 70, 30, 30))
        self.label_memos.setText("")
        self.label_memos.setObjectName("label_memos")
        self.label_selections = QtWidgets.QLabel(self.groupBox)
        self.label_selections.setGeometry(QtCore.QRect(330, 20, 611, 28))
        self.label_selections.setObjectName("label_selections")
        self.pushButton_clear = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_clear.setGeometry(QtCore.QRect(50, 60, 32, 32))
        self.pushButton_clear.setText("")
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.pushButton_exporttext = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_exporttext.setGeometry(QtCore.QRect(90, 60, 32, 32))
        self.pushButton_exporttext.setText("")
        self.pushButton_exporttext.setObjectName("pushButton_exporttext")
        self.pushButton_run = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_run.setGeometry(QtCore.QRect(10, 60, 32, 32))
        self.pushButton_run.setText("")
        self.pushButton_run.setObjectName("pushButton_run")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(328, 53, 101, 17))
        self.label.setObjectName("label")
        self.label_stats = QtWidgets.QLabel(self.groupBox)
        self.label_stats.setGeometry(QtCore.QRect(440, 53, 511, 61))
        self.label_stats.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_stats.setWordWrap(True)
        self.label_stats.setObjectName("label_stats")
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog_reportCompareCoderFile)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(self.groupBox_2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.splitter_vert = QtWidgets.QSplitter(self.splitter)
        self.splitter_vert.setOrientation(QtCore.Qt.Vertical)
        self.splitter_vert.setObjectName("splitter_vert")
        self.listWidget_files = QtWidgets.QListWidget(self.splitter_vert)
        self.listWidget_files.setObjectName("listWidget_files")
        self.treeWidget = QtWidgets.QTreeWidget(self.splitter_vert)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "Code Tree")
        self.textEdit = QtWidgets.QTextEdit(self.splitter)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)

        self.retranslateUi(Dialog_reportCompareCoderFile)
        QtCore.QMetaObject.connectSlotsByName(Dialog_reportCompareCoderFile)
        Dialog_reportCompareCoderFile.setTabOrder(self.comboBox_coders, self.treeWidget)
        Dialog_reportCompareCoderFile.setTabOrder(self.treeWidget, self.textEdit)

    def retranslateUi(self, Dialog_reportCompareCoderFile):
        _translate = QtCore.QCoreApplication.translate
        Dialog_reportCompareCoderFile.setWindowTitle(_translate("Dialog_reportCompareCoderFile", "Reports"))
        self.label_2.setText(_translate("Dialog_reportCompareCoderFile", "Coders:"))
        self.label_exports.setToolTip(_translate("Dialog_reportCompareCoderFile", "<html><head/><body><p>Export</p></body></html>"))
        self.label_title.setToolTip(_translate("Dialog_reportCompareCoderFile", "To compare coding.\n"
"Select two coders, one file, one code."))
        self.label_title.setText(_translate("Dialog_reportCompareCoderFile", "Coder comparisons by file"))
        self.label_matrix.setToolTip(_translate("Dialog_reportCompareCoderFile", "<html><head/><body><p>Matrix options</p></body></html>"))
        self.label_memos.setToolTip(_translate("Dialog_reportCompareCoderFile", "Memo reporting options"))
        self.label_selections.setText(_translate("Dialog_reportCompareCoderFile", "Coders selected"))
        self.pushButton_clear.setToolTip(_translate("Dialog_reportCompareCoderFile", "<html><head/><body><p>Clear selection</p></body></html>"))
        self.pushButton_exporttext.setToolTip(_translate("Dialog_reportCompareCoderFile", "<html><head/><body><p>Export text file</p></body></html>"))
        self.pushButton_run.setToolTip(_translate("Dialog_reportCompareCoderFile", "<html><head/><body><p>Run comparison</p></body></html>"))
        self.label.setText(_translate("Dialog_reportCompareCoderFile", "Statistics:"))
        self.label_stats.setText(_translate("Dialog_reportCompareCoderFile", "statistics"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_reportCompareCoderFile = QtWidgets.QDialog()
    ui = Ui_Dialog_reportCompareCoderFile()
    ui.setupUi(Dialog_reportCompareCoderFile)
    Dialog_reportCompareCoderFile.show()
    sys.exit(app.exec_())
