from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_AreaRiservataAmministratore(object):
    def setupUi(self, AreaRiservataAmministratore):
        AreaRiservataAmministratore.setObjectName("AreaRiservataAmministratore")
        AreaRiservataAmministratore.resize(766, 547)
        self.pushButton = QtWidgets.QPushButton(parent=AreaRiservataAmministratore)
        self.pushButton.setGeometry(QtCore.QRect(150, 80, 180, 70))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=AreaRiservataAmministratore)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 180, 180, 70))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=AreaRiservataAmministratore)
        self.pushButton_3.setGeometry(QtCore.QRect(150, 280, 180, 70))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=AreaRiservataAmministratore)
        self.pushButton_4.setGeometry(QtCore.QRect(420, 180, 180, 70))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(parent=AreaRiservataAmministratore)
        self.pushButton_5.setGeometry(QtCore.QRect(420, 80, 180, 70))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(parent=AreaRiservataAmministratore)
        self.pushButton_6.setGeometry(QtCore.QRect(420, 280, 180, 70))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(parent=AreaRiservataAmministratore)
        self.pushButton_7.setGeometry(QtCore.QRect(300, 370, 180, 70))
        self.pushButton_7.setObjectName("pushButton_7")
        self.label = QtWidgets.QLabel(parent=AreaRiservataAmministratore)
        self.label.setGeometry(QtCore.QRect(250, 20, 341, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(AreaRiservataAmministratore)
        QtCore.QMetaObject.connectSlotsByName(AreaRiservataAmministratore)

    def retranslateUi(self, AreaRiservataAmministratore):
        _translate = QtCore.QCoreApplication.translate
        AreaRiservataAmministratore.setWindowTitle(_translate("AreaRiservataAmministratore", "Form"))
        self.pushButton.setText(_translate("AreaRiservataAmministratore", "Osservatori disponibili"))
        self.pushButton_2.setText(_translate("AreaRiservataAmministratore", "Arbitri disponibili"))
        self.pushButton_3.setText(_translate("AreaRiservataAmministratore", "Assistenti disponibili"))
        self.pushButton_4.setText(_translate("AreaRiservataAmministratore", "Aggiorna storico"))
        self.pushButton_5.setText(_translate("AreaRiservataAmministratore", "Assegnazione gara"))
        self.pushButton_6.setText(_translate("AreaRiservataAmministratore", "Modifica associato"))
        self.pushButton_7.setText(_translate("AreaRiservataAmministratore", "Visualizza profilo"))
        self.label.setText(_translate("AreaRiservataAmministratore", "AREA AMMINISTRATORE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AreaRiservataAmministratore = QtWidgets.QWidget()
    ui = Ui_AreaRiservataAmministratore()
    ui.setupUi(AreaRiservataAmministratore)
    AreaRiservataAmministratore.show()
    sys.exit(app.exec())
