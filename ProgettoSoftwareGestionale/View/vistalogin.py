from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        # Imposta il nome e le dimensioni del widget principale
        Form.setObjectName("Form")
        Form.resize(890, 562)

        # Ottieni le dimensioni del widget principale
        window_width = Form.frameGeometry().width()
        window_height = Form.frameGeometry().height()

        # Dimensioni del widget interno
        widget_width = 161
        widget_height = 28

        # Calcola l'offset per centrare gli elementi verso destra
        offset = 50

        # Calcola le posizioni centrali orizzontali e verticali
        center_horizontal = int((window_width - widget_width) / 2) + offset
        center_vertical = int((window_height - widget_height) / 2)

        # Aggiungi un pulsante "Accedi"
        self.btnaccedi = QtWidgets.QPushButton(parent=Form)
        self.btnaccedi.setGeometry(QtCore.QRect(center_horizontal - 100, center_vertical, 161, 28))
        self.btnaccedi.setObjectName("btnaccedi")

        # Aggiungi un pulsante "Cancella"
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(center_horizontal + 100, center_vertical, 161, 28))
        self.pushButton.setObjectName("pushButton")

        # Aggiungi una label per il titolo
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(center_horizontal - 145, center_vertical - 150, 371, 32))
        self.label.setObjectName("label")
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)  # Imposta l'allineamento al centro

        # Aggiungi una label per "Codice Meccanografico"
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(
            QtCore.QRect(center_horizontal - 300, center_vertical - 100, 161, 32))  # Modifica la posizione orizzontale
        self.label_2.setObjectName("label_2")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)

        # Aggiungi una casella di testo per inserire il codice meccanografico
        self.lineEdit = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit.setGeometry(QtCore.QRect(center_horizontal - 125, center_vertical - 100, 400,
                                               32))  # Modifica la posizione e la dimensione orizzontale
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)

        # Aggiungi una label per "Password"
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(
            QtCore.QRect(center_horizontal - 255, center_vertical - 50, 71, 32))  # Modifica la posizione orizzontale
        self.label_3.setObjectName("label_3")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)

        # Aggiungi una casella di testo per inserire la password
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(center_horizontal - 125, center_vertical - 50, 400,
                                                 32))  # Modifica la posizione e la dimensione orizzontale
        self.lineEdit_2.setObjectName("lineEdit_2")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)

        # Connessione degli elementi grafici
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btnaccedi.setText(_translate("Form", "Accedi"))
        self.pushButton.setText(_translate("Form", "Cancella"))
        self.label.setText(_translate("Form", "ACCEDI ALL'AREA RISERVATA"))
        self.label_2.setText(_translate("Form", "Codice Meccanografico"))
        self.label_3.setText(_translate("Form", "Password"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())

#!!!!!!!
# Ho messo i commenti ovunque cosi capisci cos'ho fatto, se hai dubbi scrivimi
#!!!!!!!