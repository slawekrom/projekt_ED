from PyQt5 import QtCore, QtGui, QtWidgets


from PyQt5 import QtCore, QtGui, QtWidgets


class NormDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(454, 308)
        self.comboBoxColumn = QtWidgets.QComboBox(Dialog)
        self.comboBoxColumn.setGeometry(QtCore.QRect(160, 10, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBoxColumn.setFont(font)
        self.comboBoxColumn.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 10, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.cancelButton = QtWidgets.QPushButton(Dialog)
        self.cancelButton.setGeometry(QtCore.QRect(340, 260, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cancelButton.setFont(font)
        self.cancelButton.setObjectName("cancelButton")
        self.okButton = QtWidgets.QPushButton(Dialog)
        self.okButton.setGeometry(QtCore.QRect(230, 260, 91, 31))
        self.okButton.setObjectName("okButton")
        self.checkBoxNormalizeAll = QtWidgets.QCheckBox(Dialog)
        self.checkBoxNormalizeAll.setGeometry(QtCore.QRect(60, 100, 201, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBoxNormalizeAll.setFont(font)
        self.checkBoxNormalizeAll.setObjectName("checkBoxNormalizeAll")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Kolumna"))
        self.cancelButton.setText(_translate("Dialog", "Anuluj"))
        self.okButton.setText(_translate("Dialog", "OK"))
        self.checkBoxNormalizeAll.setText(_translate("Dialog", "Normalizuj wszystkie atrybuty"))
