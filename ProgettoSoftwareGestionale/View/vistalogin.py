from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_FrameAccesso(object):
    def setupUi(self, FrameAccesso):
        FrameAccesso.setObjectName("FrameAccesso")
        FrameAccesso.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        FrameAccesso.resize(640, 480)
        FrameAccesso.setMaximumSize(QtCore.QSize(640, 480))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("download.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        FrameAccesso.setWindowIcon(icon)
        FrameAccesso.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        FrameAccesso.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.labelInserimento = QtWidgets.QLabel(parent=FrameAccesso)
        self.labelInserimento.setGeometry(QtCore.QRect(230, 30, 179, 32))
        self.labelInserimento.setBaseSize(QtCore.QSize(1, 0))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        self.labelInserimento.setFont(font)
        self.labelInserimento.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.labelInserimento.setAutoFillBackground(True)
        self.labelInserimento.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.labelInserimento.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelInserimento.setObjectName("labelInserimento")
        self.label = QtWidgets.QLabel(parent=FrameAccesso)
        self.label.setGeometry(QtCore.QRect(110, 130, 141, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=FrameAccesso)
        self.label_2.setGeometry(QtCore.QRect(110, 210, 141, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(parent=FrameAccesso)
        self.lineEdit.setGeometry(QtCore.QRect(350, 128, 201, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=FrameAccesso)
        self.lineEdit_2.setGeometry(QtCore.QRect(350, 208, 201, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(parent=FrameAccesso)
        self.pushButton.setGeometry(QtCore.QRect(250, 290, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(FrameAccesso)
        QtCore.QMetaObject.connectSlotsByName(FrameAccesso)

    def retranslateUi(self, FrameAccesso):
        _translate = QtCore.QCoreApplication.translate
        FrameAccesso.setWindowTitle(_translate("FrameAccesso", "LoginAreariservata"))
        self.labelInserimento.setText(_translate("FrameAccesso", "INSERISCI LE TUE CREDENZIALI"))
        self.label.setText(_translate("FrameAccesso", "Codice Meccanografico:"))
        self.label_2.setText(_translate("FrameAccesso", "Password:"))
        self.pushButton.setText(_translate("FrameAccesso", "Accedi"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrameAccesso = QtWidgets.QFrame()
    ui = Ui_FrameAccesso()
    ui.setupUi(FrameAccesso)
    FrameAccesso.show()
    sys.exit(app.exec())

