from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        width = screen_geometry.width()
        height = screen_geometry.height()

        Form.resize(width, height)
        self.btnaccedi = QtWidgets.QPushButton(parent=Form)
        self.btnaccedi.setGeometry(QtCore.QRect(int(width*0.2), int(height*0.6), 161, 28))  # (x,y,larghezza,altezza)
        self.btnaccedi.setObjectName("btnaccedi")
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(int(width*0.55), int(height*0.6), 161, 28))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit.setGeometry(QtCore.QRect(int(width*0.47), int(height*0.23), 211, 22))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(int(width*0.29), int(height*0.07), 401, 31))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(int(width*0.17), int(height*0.23), 161, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(int(width*0.17), int(height*0.37), 81, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(int(width*0.47), int(height*0.37), 211, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # Centra la finestra sullo schermo
        qr = Form.frameGeometry()
        cp = QApplication.primaryScreen().availableGeometry().center()
        qr.moveCenter(cp)
        Form.move(qr.topLeft())

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btnaccedi.setText(
            _translate("Form", "Accedi"))  # bottone accedi, il sistema dovrà verificare l'autenticità delle credenziali
        self.pushButton.setText(_translate("Form", "Cancella"))  # serve per pulire le caselle di testo
        self.label.setText(_translate("Form", "ACCEDI ALL\'AREA RISERVATA"))
        self.label_2.setText(_translate("Form", "Codice meccanografico:"))
        self.label_3.setText(_translate("Form", "Password:"))

class MyWidget(QWidget):
    def __init__(self, parent=None):
        super(MyWidget, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            self.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.showFullScreen()
    sys.exit(app.exec())