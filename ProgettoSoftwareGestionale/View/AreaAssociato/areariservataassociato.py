from PyQt6 import QtCore, QtGui, QtWidgets


def create_push_button(parent, geometry, object_name):
    button = QtWidgets.QPushButton(parent=parent)
    button.setGeometry(geometry)
    button.setObjectName(object_name)
    return button


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(890, 562)
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(480, 40, 55, 16))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(340, 30, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = create_push_button(Form, QtCore.QRect(240, 100, 180, 90), "pushButton")
        self.pushButton_2 = create_push_button(Form, QtCore.QRect(460, 100, 180, 90), "pushButton_2")
        self.pushButton_3 = create_push_button(Form, QtCore.QRect(240, 230, 180, 90), "pushButton_3")
        self.pushButton_4 = create_push_button(Form, QtCore.QRect(460, 230, 180, 90), "pushButton_4")
        self.pushButton_5 = create_push_button(Form, QtCore.QRect(240, 360, 180, 90), "pushButton_5")
        self.pushButton_6 = create_push_button(Form, QtCore.QRect(460, 360, 180, 90), "pushButton_6")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "AREA ASSOCIATO"))
        self.pushButton.setText(_translate("Form", "Visualizza storico gare"))
        self.pushButton_2.setText(_translate("Form", "Visualizza gare"))
        self.pushButton_3.setText(_translate("Form", "Accettazione gara"))
        self.pushButton_4.setText(_translate("Form", "Scarica modulo referto"))
        self.pushButton_5.setText(_translate("Form", "Carica modulo referto"))
        self.pushButton_6.setText(_translate("Form", "Carica certificato medico"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
