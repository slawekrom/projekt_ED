from PyQt5 import QtCore, QtGui, QtWidgets


class Vectorize_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(958, 676)
        self.drawButton = QtWidgets.QPushButton(Dialog)
        self.drawButton.setGeometry(QtCore.QRect(740, 80, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.drawButton.setFont(font)
        self.drawButton.setObjectName("drawButton")
        self.addButton = QtWidgets.QPushButton(Dialog)
        self.addButton.setGeometry(QtCore.QRect(20, 80, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.addButton.setFont(font)
        self.addButton.setObjectName("addButton")
        self.tableView = QtWidgets.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(10, 130, 941, 481))
        self.tableView.setObjectName("tableView")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 0, 721, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.newValues = QtWidgets.QLineEdit(Dialog)
        self.newValues.setGeometry(QtCore.QRect(20, 40, 691, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.newValues.setFont(font)
        self.newValues.setObjectName("newValues")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(200, 90, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.newObject_label = QtWidgets.QLabel(Dialog)
        self.newObject_label.setGeometry(QtCore.QRect(300, 90, 411, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.newObject_label.setFont(font)
        self.newObject_label.setText("")
        self.newObject_label.setObjectName("newObject_label")
        self.saveButton = QtWidgets.QPushButton(Dialog)
        self.saveButton.setGeometry(QtCore.QRect(820, 630, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.saveButton.setFont(font)
        self.saveButton.setObjectName("saveButton")
        self.filenameLabel = QtWidgets.QLineEdit(Dialog)
        self.filenameLabel.setGeometry(QtCore.QRect(520, 630, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.filenameLabel.setFont(font)
        self.filenameLabel.setObjectName("filenameLabel")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(420, 640, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.drawButton.setText(_translate("Dialog", "Wizualizacja"))
        self.addButton.setText(_translate("Dialog", "Klasyfikuj nowy obiekt"))
        self.label_2.setText(_translate("Dialog",
                                        "Dane nowego elementu - wprować dane nowego elementu, wartość kolejych atrybutów oddzielone spacją"))
        self.label.setText(_translate("Dialog", "Nowy obiekt to:"))
        self.saveButton.setText(_translate("Dialog", "Zapisz"))
        self.label_3.setText(_translate("Dialog", "Nazwa pliku"))

