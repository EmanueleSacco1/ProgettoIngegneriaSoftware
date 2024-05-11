from PyQt6 import QtCore, QtGui, QtWidgets

def create_push_button(parent, geometry, object_name):
    button = QtWidgets.QPushButton(parent=parent)
    button.setGeometry(geometry)
    button.setObjectName(object_name)
    return button

class Ui_AreaRiservataAmministratore(object):
    def setupUi(self, AreaRiservataAmministratore):
        AreaRiservataAmministratore.setObjectName("AreaRiservataAmministratore")
        AreaRiservataAmministratore.resize(890, 562)
        self.pushButton = create_push_button(AreaRiservataAmministratore, QtCore.QRect(240, 100, 180, 90), "pushButton")
        self.pushButton_2 = create_push_button(AreaRiservataAmministratore, QtCore.QRect(460, 100, 180, 90), "pushButton_2")
        self.pushButton_3 = create_push_button(AreaRiservataAmministratore, QtCore.QRect(240, 230, 180, 90), "pushButton_3")
        self.pushButton_4 = create_push_button(AreaRiservataAmministratore, QtCore.QRect(460, 230, 180, 90), "pushButton_4")
        self.pushButton_5 = create_push_button(AreaRiservataAmministratore, QtCore.QRect(240, 360, 180, 90), "pushButton_5")
        self.pushButton_6 = create_push_button(AreaRiservataAmministratore, QtCore.QRect(460, 360, 180, 90), "pushButton_6")
        self.pushButton_7 = create_push_button(AreaRiservataAmministratore, QtCore.QRect(350, 460, 180, 90), "pushButton_7")
        self.label = QtWidgets.QLabel(parent=AreaRiservataAmministratore)
        self.label.setGeometry(QtCore.QRect(320, 30, 331, 51))
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
