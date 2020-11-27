from PyQt5 import QtCore, QtGui, QtWidgets


class HistogramDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(403, 214)
        self.comboBoxColumn = QtWidgets.QComboBox(Dialog)
        self.comboBoxColumn.setGeometry(QtCore.QRect(20, 10, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBoxColumn.setFont(font)
        self.comboBoxColumn.setObjectName("comboBoxColumn")
        self.okButton = QtWidgets.QPushButton(Dialog)
        self.okButton.setGeometry(QtCore.QRect(270, 60, 71, 31))
        self.okButton.setObjectName("okButton")
        self.checkBoxSets = QtWidgets.QCheckBox(Dialog)
        self.checkBoxSets.setGeometry(QtCore.QRect(40, 60, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBoxSets.setFont(font)
        self.checkBoxSets.setObjectName("checkBoxSets")
        self.lineSets = QtWidgets.QLineEdit(Dialog)
        self.lineSets.setGeometry(QtCore.QRect(200, 60, 31, 31))
        self.lineSets.setObjectName("lineSets")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.okButton.setText(_translate("Dialog", "OK"))
        self.checkBoxSets.setText(_translate("Dialog", "Podziel na przdziały "))
